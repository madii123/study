from board import Board
from dice import Dice
from game import Game
from players import Player


def main():
    players = [Player("madhu"), Player("Pankaj")]

    jumps = {1: 5, 56: 76, 8: 34, 30: 55, 40: 78, 20: 6, 18: 5, 96: 5, 77: 67}
    dice = Dice(6)

    board = Board(100, jumps)
    game = Game(players, board, dice)

    while True:
        should_move = input("roll dice? ")

        if should_move.lower() in ["y", "yes"]:
            game.move()
        else:
            print("game exited")
            break


if __name__ == "__main__":
    main()
