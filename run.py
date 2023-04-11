import random
import gspread
from google.oauth2.service_account import Credentials

# Set up Google Sheets credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Battleship')

# Load the dictionary from Google Sheets
verify = SHEET.worksheet('auth_dict')
auth_dict = {row[0]: row[1] for row in verify.get_all_values()}


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
        return 0 <= x < self.size and 0 <= y \
            < self.size and self.grid[x][y] == '.'

    def fire(self, x, y):
        """
        returns True if there is a ship at that location, otherwise False.
        if ship present at location displays 'X'.
        Otherwise, it sets the tile to '-'.
        """
        if (x, y) in self.ships:
            self.ships.remove((x, y))
            self.grid[x][y] = 'X'
            return True
        else:
            self.grid[x][y] = '-'
            return False


def get_valid_coordinate(prompt, board):
    """
    function takes a prompt and a board and repeatedly \
    prompts the user to enter valid coordinates\
    until valid coordinates are entered.\
    It returns the coordinates as a tuple.
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
            print('Invalid input. Please enter two integers \
               between 0-5 separated by a comma.')


def play_game():
    """
    Main function. Setys up and plays. Initialises player and board\
    Adds ships to the board gane and enters a loop where comuter\
    and player take turns unil no more ships
    """
    size = 5
    player_name = input('Please enter your name:\n ')
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

    # play the game
    while player_board.ships and computer_board.ships:
        print(player_board)
        x, y = get_valid_coordinate(f'{player_name}, \
            enter coordinates: ', computer_board)
        player_hit = computer_board.fire(x, y)
        if player_hit:
            print('Hit!')
        else:
            print('Miss...')
        x, y = random.randint(0, size-1), random.randint(0, size-1)
        while not player_board.is_valid(x, y):
            x, y = random.randint(0, size-1), random.randint(0, size-1)
        computer_hit = player_board.fire(x, y)
        print(f'Computer shoots at ({x},{y})')
        if computer_hit:
            print('Computer hits!')
        else:
            print('Computer misses...')


play_game()
