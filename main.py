import logic
import pygame

import settings
from vec import vec

# Load sprites
number_sprites = [pygame.image.load('Sprites/t{}.png'.format(i)) for i in range(9)]
bomb_sprite = pygame.image.load('Sprites/bomb.png')
block_sprite = pygame.image.load('Sprites/block.png')
flag_sprite = pygame.image.load('Sprites/flag.png')

def main():
    pygame.init()
    pygame.display.set_caption("Mines!")
     
    screen = pygame.display.set_mode(tuple(settings.SCREEN_SIZE))

    running = True
    ended = False

    board = logic.Board(settings.MINE_COUNT)
    draw_board(board, screen)

    while running:
    
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if ended:
                        board = logic.Board(settings.MINE_COUNT)
                        ended = False
                    else:
                        left_click(board, vec(event.pos))
                elif event.button == 3:
                    right_click(board, vec(event.pos))

                draw_board(board, screen)

                status = board.get_status()
                if status != 'Ok':
                    ended = True
                    draw_text(status, screen)

def draw_board(board, screen):
    for x, y, current_cell in board:

        pos = (vec(x, y) * settings.BLOCK_SIZE)
        draw_cell(current_cell, screen, tuple(pos))
        
    pygame.display.flip()

def draw_cell(cell, screen, position):
    if not cell.open:
        if cell.flag:
            screen.blit(flag_sprite, position)
        else:
            screen.blit(block_sprite, position)

    elif cell.bomb:
        screen.blit(bomb_sprite, position)
    else:
        screen.blit(number_sprites[cell.number], position)

def draw_text(text, screen):
    """Draws given text in the middle of """
    font = pygame.font.Font(None, settings.FONT_SIZE)

    text = font.render(text, 1, settings.TEXT_COLOR)
    text_position = settings.SCREEN_SIZE // 2 - vec(text.get_size()) // 2

    background = pygame.Surface((settings.SCREEN_SIZE.x, text.get_size()[1]))
    background.fill((0, 0, 0))
    background.set_alpha(settings.BACKGROUND_ALPHA)

    screen.blit(background, (0, text_position.y))
    screen.blit(text, tuple(text_position))
    pygame.display.flip()

def left_click(board, coords):
    actual_coords = (coords) // settings.BLOCK_SIZE
    if not logic.invalid_coords(actual_coords) and not board.get(actual_coords).flag:
        board.open_cell(actual_coords)

def right_click(board, coords):
    actual_coords = (coords) // settings.BLOCK_SIZE
    if not logic.invalid_coords(actual_coords):
        board.toggle_flag(actual_coords)

if __name__ == "__main__":
    main()
