import pygame

WIDTH, HEIGHT = 690, 675
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//ROWS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (30, 25))
