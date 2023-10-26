import pytest
from pydantic import ValidationError

from random import randint

from abc import abstractmethod, ABC
from typing import Optional, List

from pydantic import BaseModel, validator


class ShipPlacement(BaseModel):
    ship_type: str
    start: dict  # {"row": int, "column": str}
    direction: str

    @validator("start")
    def validate_start(cls, start):
        row, column = start.get("row"), start.get("column")

        if not (1 <= row <= 10):
            raise ValueError("Row must be between 1 and 10 inclusive.")

        if column not in list("ABCDEFGHIJ"):
            raise ValueError("Column must be one of A, B, C, D, E, F, G, H, I, J.")

        return start


class Turn(BaseModel):
    target: dict  # {"row": int, "column": str}


class TurnResponse(BaseModel):
    result: str
    ship_type: str


class GameStatus(BaseModel):
    is_game_over: bool
    winner: str


class Game(BaseModel):
    game_id: str
    players: list[str]
    board: dict  # This could represent the state of the game board, you might need to flesh this out further
    ships: list[ShipPlacement]  # List of ship placements for this game
    turns: list[Turn]  # List of turns that have been taken


from random import randint



class AbstractBattleship(ABC):
    SHIP_LENGTHS = {
        "carrier": 5,
        "battleship": 4,
        "cruiser": 3,
        "submarine": 3,
        "destroyer": 2,
    }

    @abstractmethod
    def create_ship_placement(self, game_id: str, placement: ShipPlacement) -> None:
        """
        Place a ship on the grid.
        """
        pass

    @abstractmethod
    def create_turn(self, game_id: str, turn: Turn) -> TurnResponse:
        """
        Players take turns to target a grid cell.
        """
        pass

    @abstractmethod
    def get_game_status(self, game_id: str) -> GameStatus:
        """
        Check if the game is over and get the winner if there's one.
        """
        pass

    @abstractmethod
    def get_winner(self, game_id: str) -> str:
        """
        Get the winner of the game.
        """
        pass

    @abstractmethod
    def get_game(self) -> Game:
        """
        Retrieve the state of the game.
        """
        pass

    @abstractmethod
    def delete_game(self, game_id: str) -> None:
        """
        Delete a game given its ID.
        """
        pass

    @abstractmethod
    def create_game(self) -> None:
        """
        Create a new game.
        """
        pass

class Battleship(AbstractBattleship):
    """
    Implementation of the Battleship game using the AbstractBattleship class.
    """

    # Dictionary to store the game boards for each player
    boards = {}

    # Dictionary to store the ships for each player
    ships = {}

    # Dictionary to store the turns for each player
    turns = {}

    # Dictionary to store the game status for each player
    game_status = {}

    # Dictionary to store the winner for each player
    winner = {}

    def create_ship_placement(self, game_id: str, placement: ShipPlacement) -> None:
        """
        Place a ship on the grid.
        """
        # Check if the game ID is valid
        if game_id not in self.boards:
            raise ValueError("Invalid game ID.")

        # Check if the ship type is valid
        if placement.ship_type not in self.SHIP_LENGTHS:
            raise ValueError("Invalid ship type.")

        # Check if the ship placement is valid
        if not self._validate_ship_placement(placement):
            raise ValueError("Invalid ship placement.")

        # Check if the ship has already been placed
        if placement.ship_type in self.ships[game_id]:
            raise ValueError("Ship has already been placed.")

        # Add the ship placement to the ships dictionary
        self.ships[game_id][placement.ship_type] = placement

    def create_turn(self, game_id: str, turn: Turn) -> TurnResponse:
        """
        Players take turns to target a grid cell.
        """
        # Check if the game ID is valid
        if game_id not in self.boards:
            raise ValueError("Invalid game ID.")

        # Check if the target is valid
        if not self._validate_target(turn.target):
            raise ValueError("Invalid target.")

        # Check if it is the player's turn
        if turn not in self.turns[game_id]:
            raise ValueError("Not your turn.")

        # Check if the target has already been hit
        if self.boards[game_id][turn.target["row"]][turn.target["column"]] == "X":
            raise ValueError("Target has already been hit.")

        # Check if the target is a hit or a miss
        if self.boards[game_id][turn.target["row"]][turn.target["column"]] == "O":
            result = "miss"
        else:
            result = "hit"
            # Update the board to show the hit
            self.boards[game_id][turn.target["row"]][turn.target["column"]] = "X"

            # Check if the ship has been sunk
            ship_type = self._check_ship_sunk(game_id, turn.target)
            if ship_type:
                return TurnResponse(result=result, ship_type=ship_type)

        # Remove the turn from the turns dictionary
        self.turns[game_id].remove(turn)

        return TurnResponse(result=result, ship_type=None)

    def get_game_status(self, game_id: str) -> GameStatus:
        """
        Check if the game is over and get the winner if there's one.
        """
        # Check if the game ID is valid
        if game_id not in self.boards:
            raise ValueError("Invalid game ID.")

        # Check if the game is over
        if self.game_status[game_id]:
            return GameStatus(is_game_over=True, winner=self.winner[game_id])
        else:
            return GameStatus(is_game_over=False, winner=None)

    def get_winner(self, game_id: str) -> str:
        """
        Get the winner of the game.
        """
        # Check if the game ID is valid
        if game_id not in self.boards:
            raise ValueError("Invalid game ID.")

        # Check if the game is over
        if not self.game_status[game_id]:
            raise ValueError("Game is not over yet.")

        return self.winner[game_id]

    def get_game(self) -> Game:
        """
        Retrieve the state of the game.
        """
        # Create a new game ID
        game_id = self._create_game_id()

        # Create the game board for each player
        self.boards[game_id] = self._create_board()
        self.boards[game_id + "_opponent"] = self._create_board()

        # Create the ships dictionary for each player
        self.ships[game_id] = {}
        self.ships[game_id + "_opponent"] = {}

        # Create the turns dictionary for each player
        self.turns[game_id] = []
        self.turns[game_id + "_opponent"] = []

        # Set the game status to False (not over)
        self.game_status[game_id] = False
        self.game_status[game_id + "_opponent"] = False

        # Set the winner to None
        self.winner[game_id] = None
        self.winner[game_id + "_opponent"] = None

        # Return the game object
        return Game(game_id=game_id, players=[game_id, game_id + "_opponent"], board=self.boards[game_id], ships=self.ships[game_id], turns=self.turns[game_id])

    def delete_game(self, game_id: str) -> None:
        """
        Delete a game given its ID.
        """
        # Check if the game ID is valid
        if game_id not in self.boards:
            raise ValueError("Invalid game ID.")

        # Delete the game from all dictionaries
        del self.boards[game_id]
        del self.boards[game_id + "_opponent"]
        del self.ships[game_id]
        del self.ships[game_id + "_opponent"]
        del self.turns[game_id]
        del self.turns[game_id + "_opponent"]
        del self.game_status[game_id]
        del self.game_status[game_id + "_opponent"]
        del self.winner[game_id]
        del self.winner[game_id + "_opponent"]

    def create_game(self) -> None:
        """
        Create a new game.
        """
        # Create a new game object
        game = self.get_game()

        # Place the ships for each player
        self._place_ships(game.game_id)
        self._place_ships(game.game_id + "_opponent")

        # Randomly choose who goes first
        first_player = game.players[randint(0, 1)]

        # Add the first player's turn to the turns dictionary
        self.turns[first_player].append(Turn(target={"row": randint(1, 10), "column": chr(randint(65, 74))}))

    def _create_game_id(self) -> str:
        """
        Create a unique game ID.
        """
        # Generate a random 6-digit number
        game_id = randint(100000, 999999)

        # Check if the game ID already exists
        if game_id in self.boards:
            # If it does, recursively call the function again to generate a new ID
            return self._create_game_id()
        else:
            return str(game_id)

    def _create_board(self) -> dict:
        """
        Create a new game board.
        """
        # Create an empty board
        board = {}

        # Loop through each row and column and add it to the board
        for row in range(1, 11):
            for column in list("ABCDEFGHIJ"):
                board[row] = {}
                board[row][column] = "O"

        return board

    def _validate_ship_placement(self, placement: ShipPlacement) -> bool:
        """
        Validate the ship placement.
        """
        # Get the starting row and column
        start_row = placement.start["row"]
        start_column = placement.start["column"]

        # Get the direction
        direction = placement.direction

        # Get the length of the ship
        ship_length = self.SHIP_LENGTHS[placement.ship_type]

        # Check if the starting row and column are valid
        if not (1 <= start_row <= 10):
            return False
        if start_column not in list("ABCDEFGHIJ"):
            return False

        # Check if the direction is valid
        if direction not in ["horizontal", "vertical"]:
            return False

        # Check if the ship will fit on the board
        if direction == "horizontal":
            if start_column > chr(74 - ship_length + 1):
                return False
        else:
            if start_row > 10 - ship_length + 1:
                return False

        return True

    def _place_ships(self, game_id: str) -> None:
        """
        Place the ships on the board for a given player.
        """
        # Loop through each ship type
        for ship_type in self.SHIP_LENGTHS:
            # Create a new ship placement object
            placement = ShipPlacement(ship_type=ship_type, start={"row": randint(1, 10), "column": chr(randint(65, 74))}, direction=["horizontal", "vertical"][randint(0, 1)])

            # Keep generating a new placement until it is valid
            while not self._validate_ship_placement(placement):
                placement = ShipPlacement(ship_type=ship_type, start={"row": randint(1, 10), "column": chr(randint(65, 74))}, direction=["horizontal", "vertical"][randint(0, 1)])

            # Add the ship placement to the ships dictionary


@pytest.fixture
def battleship_game():
    return Battleship()


@pytest.fixture
def initialized_game_id(battleship_game):
    # Create a game instance
    game_id = battleship_game.create_game()

    # Place all the ships using battleship_game's methods
    sample_ship_placements = [
        ShipPlacement(
            ship_type="carrier", start={"row": 1, "column": "A"}, direction="horizontal"
        ),
        ShipPlacement(
            ship_type="battleship",
            start={"row": 2, "column": "A"},
            direction="horizontal",
        ),
        ShipPlacement(
            ship_type="cruiser", start={"row": 3, "column": "A"}, direction="horizontal"
        ),
        ShipPlacement(
            ship_type="submarine",
            start={"row": 4, "column": "A"},
            direction="horizontal",
        ),
        ShipPlacement(
            ship_type="destroyer",
            start={"row": 5, "column": "A"},
            direction="horizontal",
        ),
    ]

    for ship_placement in sample_ship_placements:
        # Place ship using battleship_game's methods
        battleship_game.create_ship_placement(game_id, ship_placement)

    return game_id


@pytest.fixture
def game_over_fixture(battleship_game, initialized_game_id):
    # Assuming 10x10 grid, target all possible positions
    for row in range(1, 11):
        for column in list("ABCDEFGHIJ"):
            # Player 1 takes a turn
            turn = Turn(target={"row": row, "column": column})
            battleship_game.create_turn(initialized_game_id, turn)

            # Player 2 takes a turn, targeting the same position as Player 1
            battleship_game.create_turn(initialized_game_id, turn)

    # At the end of this fixture, the game should be over
    return initialized_game_id
