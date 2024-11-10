import pygame
from circleshape import CircleShape
from pygame.math import Vector2
from constants import SHOT_RADIUS,ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity_x=0, velocity_y=0):
        super().__init__(x, y, radius)
        self.velocity = Vector2(velocity_x, velocity_y)
        # Ensure self.position is defined if CircleShape doesn't.
        self.position = Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_velocity1 *= 1.2
        new_velocity2 *= 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_radius, new_velocity1.x, new_velocity1.y)
        Asteroid(self.position.x, self.position.y, new_radius, new_velocity2.x, new_velocity2.y)

class Shot(CircleShape):
    def __init__(self, position, velocity_x=0, velocity_y=0):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = Vector2(velocity_x, velocity_y)
        self.radius = SHOT_RADIUS
        self.position = Vector2(position)  # Make sure it's a Vector2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt