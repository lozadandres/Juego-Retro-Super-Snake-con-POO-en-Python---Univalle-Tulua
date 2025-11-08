from game_object import GameObject
from utils import load_and_scale_image

class Obstacle(GameObject):
    def __init__(self, position):
        super().__init__(position)
        self.image = load_and_scale_image('assets/imagenes/depositphotos_54217117-stock-photo-wood-crate-generated-hires-texture.jpg', (23, 24))

    def draw(self, screen):
        screen.blit(self.image, self.position)
