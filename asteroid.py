import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        score = SCORE_MIN_ASTEROID

        if self.radius <= ASTEROID_MIN_RADIUS:
            return score
        
        if self.radius <= ASTEROID_MID_RADIUS:
            score = SCORE_MID_ASTEROID
        else:
            score = SCORE_MAX_ASTEROID
        
        random_angle = random.uniform(20, 50)

        new_vector_1 = self.velocity.rotate(random_angle)
        new_vector_2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = new_vector_1 * 1.2
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = new_vector_2 * 1.2
        return score