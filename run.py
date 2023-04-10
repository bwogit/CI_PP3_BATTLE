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

    def __str__(self):
        """
        returns a string representation of the board, 
        which is printed when the board needs to be displayed
        """
        s = f'{self.player_name} {self.board_type}\n'
        s += '   ' + ' '.join(str(i) for i in range(self.size)) + '\n'
        for i in range(self.size):
            s += f'{i} |{"|".join(self.grid[i])}|\n'
        return s

    def mark_ship(self, x, y):
        """
        adds a ship at on the board by 
        setting the corresponding tile on the grid to 'O'
        """
        self.ships.append((x, y))
        self.grid[x][y] = 'O' 

    def has_ship(self, x, y):
        """
        returns true if has a ship on it
        """
        return (x, y) in self.ships

    def is_valid(self, x, y):
        """
        returns true if location is witihn bounds
        """
        return 0 <= x < self.size and 0 <= y < self.size and self.grid[x][y] == '.'

    def fire(self, x, y):
        """
        returns True if there is a ship at that location, otherwise False. 
        if ship present at location displays 'X'. Otherwise, it sets the tile to '-'.
        """
        if (x, y) in self.ships:
            self.ships.remove((x, y))
            self.grid[x][y] = 'X'
            return True
        else:
            self.grid[x][y] = '-'
            return False

    def get_valid_coordinates(prompt, board):
        """
        """
        while True:
            try:
                x, y = input(prompt).split(',')
                x, y = int(x), int(y)
                if not board.is_valid(x, y):
                    print('Invalid coordinates.')
                else:
                    return x, y
            except ValueError:
                print('Invalid input. Please enter two integers 0-5 separated by a comma.')
    
    def play_game():
        size = 5
        player_name = input('Please enter your name: ')
        player_board = Board(size, player_name, 'player board')
        computer_board = Board(size, 'Computer', 'computer board')

        # add player's ships
        for i in range(5):
            while True:
                x, y = random.randint(0, size-1), random.randint(0, size-1)
                if player_board.is_valid(x, y):
                    break
            player_board.mark_ship(x, y)

        # add computer's ships
        for i in range(5):
            while True:
                x, y = random.randint(0, size-1), random.randint(0, size-1)
                if computer_board.is_valid(x, y):
                    break
            computer_board.mark_ship(x, y)            