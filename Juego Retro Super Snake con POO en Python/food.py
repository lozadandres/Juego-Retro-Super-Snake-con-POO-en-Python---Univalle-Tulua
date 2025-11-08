from game_object import GameObject
from utils import load_and_scale_image

class Food(GameObject):
    def __init__(self, position):
        super().__init__(position)
        self.image = load_and_scale_image('assets/imagenes/Red-Apple-icon.png', (25, 25))

    def draw(self, screen):
        screen.blit(self.image, self.position)
