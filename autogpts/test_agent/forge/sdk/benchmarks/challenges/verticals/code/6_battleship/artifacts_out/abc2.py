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
    def __init__(self):
        self.games = {}

    def create_ship_placement(self, game_id: str, placement: ShipPlacement) -> None:
        """
        Place a ship on the grid.
        """
        # Check if game exists
        if game_id not in self.games:
            raise ValueError("Game does not exist.")

        # Check if ship placement is valid
        if placement.ship_type not in self.SHIP_LENGTHS:
            raise ValueError("Invalid ship type.")

        # Check if ship placement is within grid boundaries
        start_row = placement.start["row"]
        start_col = placement.start["column"]
        direction = placement.direction
        ship_length = self.SHIP_LENGTHS[placement.ship_type]

        if direction == "horizontal":
            if start_col + ship_length > 10:
                raise ValueError("Ship placement is out of bounds.")
        elif direction == "vertical":
            if start_row + ship_length > 10:
                raise ValueError("Ship placement is out of bounds.")

        # Check if ship placement overlaps with existing ships
        for ship in self.games[game_id]["ships"]:
            # Get coordinates of existing ship
            existing_start_row = ship.start["row"]
            existing_start_col = ship.start["column"]
            existing_direction = ship.direction
            existing_ship_length = self.SHIP_LENGTHS[ship.ship_type]

            # Check for overlap
            if direction == "horizontal":
                if start_row == existing_start_row and start_col <= existing_start_col + existing_ship_length:
                    raise ValueError("Ship placement overlaps with existing ship.")
            elif direction == "vertical":
                if start_col == existing_start_col and start_row <= existing_start_row + existing_ship_length:
                    raise ValueError("Ship placement overlaps with existing ship.")

        # Add ship placement to game
        self.games[game_id]["ships"].append(placement)

    def create_turn(self, game_id: str, turn: Turn) -> TurnResponse:
        """
        Players take turns to target a grid cell.
        """
        # Check if game exists
        if game_id not in self.games:
            raise ValueError("Game does not exist.")

        # Check if game is over
        if self.games[game_id]["is_game_over"]:
            raise ValueError("Game is already over.")

        # Check if turn is valid
        target_row = turn.target["row"]
        target_col = turn.target["column"]

        if target_row not in range(1, 11) or target_col not in list("ABCDEFGHIJ"):
            raise ValueError("Invalid target.")

        # Check if target has already been hit
        for hit in self.games[game_id]["hits"]:
            if hit["row"] == target_row and hit["column"] == target_col:
                raise ValueError("Target has already been hit.")

        # Check if target is a hit or miss
        for ship in self.games[game_id]["ships"]:
            # Get coordinates of existing ship
            existing_start_row = ship.start["row"]
            existing_start_col = ship.start["column"]
            existing_direction = ship.direction
            existing_ship_length = self.SHIP_LENGTHS[ship.ship_type]

            # Check for hit
            if existing_direction == "horizontal":
                if target_row == existing_start_row and target_col in range(existing_start_col, existing_start_col + existing_ship_length):
                    self.games[game_id]["hits"].append({"row": target_row, "column": target_col})
                    # Check if ship has been sunk
                    if len(self.games[game_id]["hits"]) == existing_ship_length:
                        self.games[game_id]["sunk_ships"].append(ship.ship_type)
                        return TurnResponse(result="hit", ship_type=ship.ship_type)
                    else:
                        return TurnResponse(result="hit", ship_type=None)
            elif existing_direction == "vertical":
                if target_col == existing_start_col and target_row in range(existing_start_row, existing_start_row + existing_ship_length):
                    self.games[game_id]["hits"].append({"row": target_row, "column": target_col})
                    # Check if ship has been sunk
                    if len(self.games[game_id]["hits"]) == existing_ship_length:
                        self.games[game_id]["sunk_ships"].append(ship.ship_type)
                        return TurnResponse(result="hit", ship_type=ship.ship_type)
                    else:
                        return TurnResponse(result="hit", ship_type=None)

        # If no hit, add target to misses
        self.games[game_id]["misses"].append({"row": target_row, "column": target_col})
        return TurnResponse(result="miss", ship_type=None)

    def get_game_status(self, game_id: str) -> GameStatus:
        """
        Check if the game is over and get the winner if there's one.
        """
        # Check if game exists
        if game_id not in self.games:
            raise ValueError("Game does not exist.")

        # Check if game is over
        if self.games[game_id]["is_game_over"]:
            return GameStatus(is_game_over=True, winner=self.games[game_id]["winner"])
        else:
            return GameStatus(is_game_over=False, winner=None)

    def get_winner(self, game_id: str) -> str:
        """
        Get the winner of the game.
        """
        # Check if game exists
        if game_id not in self.games:
            raise ValueError("Game does not exist.")

        # Check if game is over
        if not self.games[game_id]["is_game_over"]:
            raise ValueError("Game is not over yet.")

        # Return winner
        return self.games[game_id]["winner"]

    def get_game(self, game_id: str) -> Game:
        """
        Retrieve the state of the game.
        """
        # Check if game exists
        if game_id not in self.games:
            raise ValueError("Game does not exist.")

        # Return game
        return self.games[game_id]

    def delete_game(self, game_id: str) -> None:
        """
        Delete a game given its ID.
        """
        # Check if game exists
        if game_id not in self.games:
            raise ValueError("Game does not exist.")

        # Delete game
        del self.games[game_id]

    def create_game(self) -> str:
        """
        Create a new game.
        """
        # Generate game ID
        game_id = str(randint(10000, 99999))

        # Create game
        self.games[game_id] = {
            "players": [],
            "board": {},
            "ships": [],
            "turns": [],
            "hits": [],
            "misses": [],
            "sunk_ships": [],
            "is_game_over": False,
            "winner": None
        }

        return game_id



# Create a new game
battleship = Battleship()
game_id = battleship.create_game()

# Get the game state
game = battleship.get_game(game_id)

# Check if the game is over
game_status = battleship.get_game_status(game.game_id)
assert game_status.is_game_over == False

# Place a ship on the grid
ship_placement = ShipPlacement(
    ship_type="carrier",
    start={"row": 1, "column": "A"},
    direction="horizontal"
)
battleship.create_ship_placement(game.game_id, ship_placement)

# Take a turn
turn = Turn(
    target={"row": 1, "column": "A"}
)
turn_response = battleship.create_turn(game.game_id, turn)
assert turn_response.result == "hit"
assert turn_response.ship_type == "carrier"

# Check if the game is over
game_status = battleship.get_game_status(game.game_id)
assert game_status.is_game_over == False

# Place another ship on the grid
ship_placement = ShipPlacement(
    ship_type="battleship",
    start={"row": 2, "column": "A"},
    direction="horizontal"
)
battleship.create_ship_placement(game.game_id, ship_placement)

# Take another turn
turn = Turn(
    target={"row": 2, "column": "A"}
)
turn_response = battleship.create_turn(game.game_id, turn)
assert turn_response.result == "hit"
assert turn_response.ship_type == "battleship"

# Check if the game is over
game_status = battleship.get_game_status(game.game_id)
assert game_status.is_game_over == True

# Get the winner
winner = battleship.get_winner(game.game_id)
assert winner == "Player 1"

# Delete the game
battleship.delete_game(game.game_id)

# Check if the game still exists
game = battleship.get_game()
assert game == None
