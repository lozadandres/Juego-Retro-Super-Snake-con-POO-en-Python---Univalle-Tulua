import pygame
from game_object import GameObject
from utils import load_and_scale_image, CELL_SIZE, WHITE

class Snake(GameObject):
    def __init__(self, position):
        super().__init__(position)
        self.directions = {
            'UP': pygame.Vector2(0, -1),
            'DOWN': pygame.Vector2(0, 1),
            'LEFT': pygame.Vector2(-1, 0),
            'RIGHT': pygame.Vector2(1, 0)
        }
        self.body = [position, position - pygame.Vector2(CELL_SIZE, 0)]
        self.direction = pygame.Vector2(1, 0)
        self.growing = False
        self.speed_boost = False
        self.head_image = load_and_scale_image("assets/imagenes/cabeza2.png", (23, 24))
        self.body_image = load_and_scale_image("assets/imagenes/body2.png", (21.5, 23))
        self.tail_image = load_and_scale_image("assets/imagenes/cola2.png", (21.5, 24))

    def move(self):
        head_position = self.body[0] + self.direction * CELL_SIZE
        if self.growing:
            self.body = [head_position] + self.body
            self.growing = False
        else:
            self.body = [head_position] + self.body[:-1]

    def grow(self):
        self.growing = True

    def draw(self, screen):
        for segment in self.body[1:-1]:
            screen.blit(self.body_image, segment)

        head_pos = self.body[0]
        rotated_head_image = pygame.transform.rotate(self.head_image, self._directions_to_angle())
        screen.blit(rotated_head_image, head_pos)

        tail_pos = self.body[-1]
        opposite_direction = -self.direction
        rotated_tail_image = pygame.transform.rotate(self.tail_image, self._directions_to_angle(opposite_direction))
        screen.blit(rotated_tail_image, tail_pos)

        tail_direction = self.body[-2] - self.body[-1]
        if tail_direction != pygame.Vector2(0, 0):
            tail_direction = tail_direction.normalize()
            angle = self._directions_to_angle(-tail_direction)
            rotated_tail_image = pygame.transform.rotate(self.tail_image, angle)
            screen.blit(rotated_tail_image, self.body[-1])

        eye_offset = [(18, 10), (10, 10)] if self.direction.x == 0 else [(12, 5), (12, 15)]
        for offset in eye_offset:
            eye_pos = (head_pos[0] + offset[0], head_pos[1] + offset[1])
            pygame.draw.circle(screen, WHITE, eye_pos, 2)

    def _directions_to_angle(self, direction=None):
        if direction is None:
            direction = self.direction
        if direction == pygame.Vector2(1, 0):
            return 270
        elif direction == pygame.Vector2(-1, 0):
            return 90
        elif direction == pygame.Vector2(0, -1):
            return 0
        elif direction == pygame.Vector2(0, 1):
            return 180

    def change_direction(self, direction):
        if direction in self.directions:
            new_direction = self.directions[direction]
            opposite_direction = -self.direction
            if new_direction != opposite_direction:
                self.direction = new_direction
