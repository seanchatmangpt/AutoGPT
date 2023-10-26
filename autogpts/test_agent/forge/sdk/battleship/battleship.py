from typing import Dict

from forge.sdk.battleship.abstract_class import (
    AbstractBattleship,
    Game,
    GameStatus,
    ShipPlacement,
    Turn,
    TurnResponse,
)


from random import randint

class Battleship(AbstractBattleship):
    """
    Implementation of the Battleship game.
    """

    def __init__(self):
        self.games = {} # dictionary to store all games
        self.ships = {} # dictionary to store all ships
        self.turns = {} # dictionary to store all turns

    def create_ship_placement(self, game_id: str, placement: ShipPlacement) -> None:
        """
        Place a ship on the grid.
        """
        # check if game exists
        if game_id not in self.games:
            raise ValueError("Game does not exist.")

        # check if ship type is valid
        if placement.ship_type not in self.SHIP_LENGTHS:
            raise ValueError("Invalid ship type.")

        # check if ship placement is valid
        start_row = placement.start["row"]
        start_column = placement.start["column"]
        direction = placement.direction

        # check if start row and column are within grid boundaries
        if not (1 <= start_row <= 10):
            raise ValueError("Row must be between 1 and 10 inclusive.")
        if start_column not in list("ABCDEFGHIJ"):
            raise ValueError("Column must be one of A, B, C, D, E, F, G, H, I, J.")

        # check if ship placement is within grid boundaries
        if direction == "horizontal":
            end_column = chr(ord(start_column) + self.SHIP_LENGTHS[placement.ship_type] - 1)
            if end_column not in list("ABCDEFGHIJ"):
                raise ValueError("Ship placement is out of bounds.")
        elif direction == "vertical":
            end_row = start_row + self.SHIP_LENGTHS[placement.ship_type] - 1
            if end_row > 10:
                raise ValueError("Ship placement is out of bounds.")
        else:
            raise ValueError("Invalid direction.")

        # check if ship overlaps with existing ships
        for ship in self.ships[game_id]:
            # check if ship is horizontal
            if ship.direction == "horizontal":
                # check if rows match
                if ship.start["row"] == start_row:
                    # check if columns overlap
                    if start_column <= ship.start["column"] <= end_column or start_column <= chr(ord(ship.start["column"]) + self.SHIP_LENGTHS[ship.ship_type] - 1) <= end_column:
                        raise ValueError("Ship placement overlaps with existing ship.")
            # check if ship is vertical
            elif ship.direction == "vertical":
                # check if columns match
                if ship.start["column"] == start_column:
                    # check if rows overlap
                    if start_row <= ship.start["row"] <= end_row or start_row <= ship.start["row"] + self.SHIP_LENGTHS[ship.ship_type] - 1 <= end_row:
                        raise ValueError("Ship placement overlaps with existing ship.")

        # add ship placement to list of ships for the game
        self.ships[game_id].append(placement)

    def create_turn(self, game_id: str, turn: Turn) -> TurnResponse:
        """
        Players take turns to target a grid cell.
        """
        # check if game exists
        if game_id not in self.games:
            raise ValueError("Game does not exist.")

        # check if game is over
        if self.games[game_id].is_game_over:
            raise ValueError("Game is already over.")

        # check if target is valid
        target_row = turn.target["row"]
        target_column = turn.target["column"]

        # check if target is within grid boundaries
        if not (1 <= target_row <= 10):
            raise ValueError("Row must be between 1 and 10 inclusive.")
        if target_column not in list("ABCDEFGHIJ"):
            raise ValueError("Column must be one of A, B, C, D, E, F, G, H, I, J.")

        # check if target has already been hit
        if (target_row, target_column) in self.turns[game_id]:
            raise ValueError("Target has already been hit.")

        # check if target hits a ship
        for ship in self.ships[game_id]:
            # check if target hits a ship's square
            if ship.direction == "horizontal":
                if ship.start["row"] == target_row and ship.start["column"] <= target_column <= chr(ord(ship.start["column"]) + self.SHIP_LENGTHS[ship.ship_type] - 1):
                    # add target to list of turns for the game
                    self.turns[game_id].append((target_row, target_column))
                    # check if ship has been sunk
                    if all((target_row, column) in self.turns[game_id] for column in range(ord(ship.start["column"]), ord(ship.start["column"]) + self.SHIP_LENGTHS[ship.ship_type])):
                        # announce sinking of ship
                        return TurnResponse(result="hit", ship_type=ship.ship_type)
                    else:
                        return TurnResponse(result="hit", ship_type=None)
            elif ship.direction == "vertical":
                if ship.start["column"] == target_column and ship.start["row"] <= target_row <= ship.start["row"] + self.SHIP_LENGTHS[ship.ship_type] - 1:
                    # add target to list of turns for the game
                    self.turns[game_id].append((target_row, target_column))
                    # check if ship has been sunk
                    if all((row, target_column) in self.turns[game_id] for row in range(ship.start["row"], ship.start["row"] + self.SHIP_LENGTHS[ship.ship_type])):
                        # announce sinking of ship
                        return TurnResponse(result="hit", ship_type=ship.ship_type)
                    else:
                        return TurnResponse(result="hit", ship_type=None)

        # add target to list of turns for the game
        self.turns[game_id].append((target_row, target_column))
        return TurnResponse(result="miss", ship_type=None)

    def get_game_status(self, game_id: str) -> GameStatus:
        """
        Check if the game is over and get the winner if there's one.
        """
        # check if game exists
        if game_id not in self.games:
            raise ValueError("Game does not exist.")

        # check if game is over
        if self.games[game_id].is_game_over:
            return GameStatus(is_game_over=True, winner=self.games[game_id].winner)
        else:
            return GameStatus(is_game_over=False, winner=None)

    def get_winner(self, game_id: str) -> str:
        """
        Get the winner of the game.
        """
        # check if game exists
        if game_id not in self.games:
            raise ValueError("Game does not exist.")

        # check if game is over
        if not self.games[game_id].is_game_over:
            raise ValueError("Game is not over yet.")

        return self.games[game_id].winner

    def get_game(self, game_id: str) -> Game:
        """
        Retrieve the state of the game.
        """
        # check if game exists
        if game_id not in self.games:
            raise ValueError("Game does not exist.")

        return self.games[game_id]

    def delete_game(self, game_id: str) -> None:
        """
        Delete a game given its ID.
        """
        # check if game exists
        if game_id not in self.games:
            raise ValueError("Game does not exist.")

        # delete game from dictionaries
        del self.games[game_id]
        del self.ships[game_id]
        del self.turns[game_id]

    def create_game(self) -> str:
        """
        Create a new game.
        """
        # generate a random game id
        game_id = str(randint(100000, 999999))

        # create new game object
        new_game = Game(game_id=game_id, players=[], board={}, ships=[], turns=[])

        # add game to dictionary
        self.games[game_id] = new_game
        self.ships[game_id] = []
        self.turns[game_id] = []

        return game_id