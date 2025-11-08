import pygame
import random
from snake import Snake
from food import Food
from obstacle import Obstacle
from special_item import SpecialItem
from utils import WIDTH, HEIGHT, CELL_SIZE, WHITE, BLACK, RED, FPS

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Retro Super Snake')
        icon = pygame.image.load('assets/imagenes/Snake-icon.png')
        pygame.display.set_icon(icon)
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()
        self.reset_game()

    def reset_game(self):
        self.snake = Snake(pygame.Vector2(WIDTH // 2, HEIGHT // 2))
        self.food = self._place_food()
        self.obstacles = self._place_obstacles()
        self.special_item = None
        self.score = 0
        self.special_item_timer = 0
        self.paused = False

    def _place_food(self):
        return self._place_random_object(Food)

    def _place_obstacles(self):
        obstacles = []
        occupied_positions = set(tuple(seg) for seg in self.snake.body)
        if hasattr(self, 'food') and self.food:
            occupied_positions.add(tuple(self.food.position))
        while len(obstacles) < 15:
            x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            new_position = (x, y)
            if new_position not in occupied_positions:
                obstacles.append(Obstacle(pygame.Vector2(x, y)))
                occupied_positions.add(new_position)
        return obstacles

    def _place_special_item(self):
        return self._place_random_object(SpecialItem)

    def _place_random_object(self, obj_type):
        occupied_positions = set(tuple(seg) for seg in self.snake.body)
        if hasattr(self, 'food') and self.food:
            occupied_positions.add(tuple(self.food.position))
        if hasattr(self, 'obstacles') and self.obstacles:
            for obstacle in self.obstacles:
                occupied_positions.add(tuple(obstacle.position))

        while True:
            x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE - 1) * CELL_SIZE
            new_position = (x, y)
            if new_position not in occupied_positions:
                return obj_type(pygame.Vector2(x, y))

    def _check_collision(self):
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food = self._place_food()
            self.score += 10
            if random.randint(0, 100) < 20 and self.special_item is None:
                self.special_item = self._place_special_item()

        if self.special_item and self.snake.body[0] == self.special_item.position:
            if self.special_item.item_type == 'speed_boost':
                self.snake.speed_boost = True
                self.special_item_timer = 200
            elif self.special_item.item_type == 'score_boost':
                self.score += 50
            self.special_item = None

        if self.snake.body[0].x < 0 or self.snake.body[0].x >= WIDTH or self.snake.body[0].y < 0 or self.snake.body[0].y >= HEIGHT:
            return True

        if len(self.snake.body) != len(set(tuple(segment) for segment in self.snake.body)):
            return True

        for obstacle in self.obstacles:
            if self.snake.body[0] == obstacle.position:
                return True

        return False

    def _update(self):
        if self.snake.speed_boost:
            self.snake.move()
        self.snake.move()
        if self.special_item_timer > 0:
            self.special_item_timer -= 1
        else:
            self.snake.speed_boost = False
        return self._check_collision()

    def _draw(self):
        background_image = pygame.image.load("assets/imagenes/R.jpeg")
        self.screen.blit(background_image, (0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
        if self.special_item:
            self.special_item.draw(self.screen)
        self._draw_score()
        pygame.display.flip()

    def _draw_score(self):
        score_text = self.font.render(f'Puntuación: {self.score}', True, WHITE)
        self.screen.blit(score_text, [10, 10])

    def _show_start_screen(self):
        background_img = pygame.image.load("assets/imagenes/inicio.png")
        self.screen.blit(background_img, (-15, -25))
        title = self.font.render('Presione cualquier tecla para comenzar', True, WHITE)
        self.screen.blit(title, [WIDTH // 4 - 40, HEIGHT // 2 + 250])
        pygame.display.flip()
        self._wait_for_key()

    def _show_game_over_screen(self):
        self.screen.fill(BLACK)
        game_over_text = self.font.render('Game Over', True, RED)
        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))

        score_text = self.font.render(f'Tu puntaje: {self.score}', True, WHITE)
        score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        restart_text1 = self.font.render('Presiona cualquier tecla', True, WHITE)
        restart_rect1 = restart_text1.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))

        restart_text2 = self.font.render('para reiniciar el juego', True, WHITE)
        restart_rect2 = restart_text2.get_rect(center=(WIDTH // 2, HEIGHT // 1.5 + 40))

        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(score_text, score_rect)
        self.screen.blit(restart_text1, restart_rect1)
        self.screen.blit(restart_text2, restart_rect2)

        pygame.display.flip()
        self._wait_for_key()

    def _wait_for_key(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    waiting = False
            pygame.time.wait(100)

    def run(self):
        self._show_start_screen()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.paused = not self.paused
                    elif not self.paused:
                        if event.key == pygame.K_w:
                            self.snake.change_direction('UP')
                        elif event.key == pygame.K_s:
                            self.snake.change_direction('DOWN')
                        elif event.key == pygame.K_a:
                            self.snake.change_direction('LEFT')
                        elif event.key == pygame.K_d:
                            self.snake.change_direction('RIGHT')

            if not self.paused:
                if self._update():
                    self._show_game_over_screen()
                    self.reset_game()
                    self._show_start_screen()

                self._draw()
                self.clock.tick(FPS + self.score // 50)
            else:
                paused_text = self.font.render('Juego Pausado', True, WHITE)
                self.screen.blit(paused_text, [WIDTH // 2.5, HEIGHT // 2.5])
                pygame.display.flip()
                pygame.time.wait(100)
        pygame.quit()
