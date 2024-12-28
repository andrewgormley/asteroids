import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast2 = Asteroid(self.position.x, self.position.y, new_radius)

            ast1.velocity = self.velocity.copy().rotate(random_angle) * 1.2
            ast2.velocity = self.velocity.copy().rotate(-random_angle) * 1.2