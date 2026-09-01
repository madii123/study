from players import Player


class Board:
    def __init__(self, size: int, jumps: dict[int, int]):
        self.size = size
        self.jumps = jumps

    def get_destination(self, player: Player, dice_value: int) -> int:
        destination = player.position + dice_value

        if destination > self.size:
            return player.position

        return self.jumps.get(destination, destination)

    def has_won(self, player: Player) -> bool:
        return player.position == self.size