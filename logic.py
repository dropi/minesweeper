from random import randint
from vec import vec
from settings import BOARD_SIZE


def invalid_coords(coords):
    """Check whether given coordinates are within board boundaries"""
    return coords.x < 0 or coords.y < 0 or coords.x >= BOARD_SIZE.x or coords.y >= BOARD_SIZE.y


class Cell:
    """A class, holding information about one cell"""
    def __init__(self):
        self.flag = False
        self.number = 0
        self.bomb = False
        self.open = False


class Board:
    """Stores game state and provides main logic"""
    
    def __init__(self, mines):
        self.board = [[Cell() for _ in range(BOARD_SIZE.x)] for _ in range(BOARD_SIZE.y)]
        self.cells_left = BOARD_SIZE.x * BOARD_SIZE.y - mines
        self.alive = True
        self.started = False
        self.mines = mines

    def get(self, coords):
        """Get cell at specified coordinates"""
        return self.board[coords.y][coords.x]

    def increment(self, coords):
        """Increment a number in a cell defined by its coordinates"""
        if invalid_coords(coords): return
        self.get(coords).number += 1

    def generate(self, start):
        """Generate a new game board"""
        mines = self.mines
        while mines > 0:

            # Choose a random location
            mine_location = vec(randint(0, BOARD_SIZE.x - 1), randint(0, BOARD_SIZE.y - 1))
            mine_cell = self.get(mine_location)

            # If there is a mine - try again
            if mine_cell.bomb:
                continue
            # If it is near the starting position - try again
            if mine_location.x - start.x <= 1 and start.x - mine_location.x <= 1:
                if mine_location.y - start.y <= 1 and start.y - mine_location.y <= 1:
                    continue

            # Place a bomb
            mine_cell.bomb = True
            mines -= 1

            # Increment all adjacent cells
            for x in range(-1, 2):
                for y in range(-1, 2):
                    self.increment(mine_location + vec(x, y))

    def open_cell(self, coords):
        """Open a cell at given coordinates"""
        if invalid_coords(coords): return
        if not self.started:
            self.generate(coords)
            self.started = True

        clicked_cell = self.get(coords)
        if clicked_cell.open: return
        clicked_cell.open = True
        if clicked_cell.bomb:
            self.alive = False
            return
        self.cells_left -= 1

        # Recursively open all adjacent cells
        if clicked_cell.number == 0:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    self.open_cell(coords + vec(x, y))

    def toggle_flag(self, coords):
        """Togle a flag of a cell at given coordinates"""
        if invalid_coords(coords): return
        clicked_cell = self.get(coords)
        if not clicked_cell.open:
            clicked_cell.flag = not clicked_cell.flag

    def get_status(self):
        """ Get status of the game board

        Possible statuses:
        'Ok'   - Game is in progress
        'Win'  - All non-mine cells are open
        'Dead' - A mine cell is open
        """
        if not self.alive: return 'Dead'
        elif self.cells_left == 0: return 'Win'
        else: return 'Ok'

    def __iter__(self):
        for y in range(BOARD_SIZE.y):
            for x in range(BOARD_SIZE.x):
                yield x, y, self.get(vec(x, y))
