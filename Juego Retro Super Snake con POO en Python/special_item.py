import random
from game_object import GameObject
from utils import load_and_scale_image

class SpecialItem(GameObject):
    def __init__(self, position):
        super().__init__(position)
        self.item_type = random.choice(['speed_boost', 'score_boost'])
        self.timer = 200
        
        if self.item_type == 'speed_boost':
            self.image = load_and_scale_image('assets/imagenes/Yellow-Apple-icon.png', (25, 25))
        elif self.item_type == 'score_boost':
            self.image = load_and_scale_image('assets/imagenes/Green-Apple-icon.png', (25, 25))

    def draw(self, screen):
        screen.blit(self.image, self.position)
