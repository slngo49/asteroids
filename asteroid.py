import pygame
from circleshape import CircleShape
from pygame.math import Vector2

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity_x=0, velocity_y=0):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.velocity = Vector2(velocity_x, velocity_y)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white",(self.x, self.y), self.radius)

    def update(self, dt):
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt

     