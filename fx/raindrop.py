import pygame
import random
from variables import BLUE

class Raindrop:
    def __init__(self, position, viewport):
        self.position = position
        self.viewport = viewport
    
    def update(self):
        x, y = self.position
        y += 5
        self.position = (x, y)

        # If the raindrop has fallen off the bottom of the screen, reset its position
        if y > self.viewport.y + self.viewport.h:
            x = random.uniform(self.viewport.x, self.viewport.x + self.viewport.w)
            y = random.uniform(self.viewport.y, self.viewport.y + self.viewport.h)
            self.position = (x, y)
        
    def draw(self, screen):
        # Draw the self.raindrops
        pygame.draw.circle(screen, BLUE, (int(self.position[0]), int(self.position[1])), 2)