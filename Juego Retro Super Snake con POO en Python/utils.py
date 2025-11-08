import pygame

# Definición de constantes
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
CAFEOS = (75, 54, 33)
CAFE = (139, 69, 19)
FPS = 10

def load_and_scale_image(filename, size):
    image = pygame.image.load(filename)
    return pygame.transform.scale(image, size)
