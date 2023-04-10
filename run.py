from random import randint

class Board:
    """
    Main board class.
    """

    def __init__(self, size, player_name, board_type):
        """
        initializing the grid with '.' characters for each tile
        """
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        self.ships = []
        self.player_name = player_name
        self.board_type = board_type
