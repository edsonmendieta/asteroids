import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = 0
    
    def draw(self, screen):
        return pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 1)
    
    def update(self, dt):
        self.position += (self.velocity *dt)