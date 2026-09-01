
from board import Board
from dice import Dice
from players import Player


class State:
    def __init__(self):
        self.winner: Player | None = None
        self.status: str = "started"


class Game:
    def __init__(self, players: list[Player], board: Board, dice: Dice):
        self.players = players
        self.board = board
        self.dice = dice

        self.current_player_index = 0
        self.winner: Player | None = None

    def _next_turn(self):
        self.current_player_index += 1
        if self.current_player_index == len(self.players):
            self.current_player_index = 0

    def move(self) -> bool:
        if self.winner:
            return False

        player = self.players[self.current_player_index]
        dice_value = self.dice.roll()

        old_position = player.position
        new_position = self.board.get_destination(player, dice_value)
        player.position = new_position

        print(f"{player.name} rolled {dice_value}: {old_position} -> {new_position}")

        if self.board.has_won(player):
            self.winner = player
            print(f"Winner: {player.name}")
            return True

        self._next_turn()
        return False
