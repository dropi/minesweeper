"""Here the game settings are stored"""
from vec import vec

# Board settings
BOARD_SIZE = vec(10, 15)
MINE_COUNT = 25
# Screen settings
BLOCK_SIZE = 40
SCREEN_SIZE = BOARD_SIZE * BLOCK_SIZE
# Text settings
FONT_SIZE = 100
TEXT_COLOR = (240, 240, 240)
BACKGROUND_ALPHA = 170