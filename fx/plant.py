import pygame
from variables import GREEN

class Plant:
    def __init__(self, position, viewport):
        self.position = position
        self.viewport = viewport
        self.growth = 0
        self.max_growth = 5
        self.growth_rate = 1
    
    def update(self):
      # Check if the plant is fully grown
      if self.growth >= self.max_growth:
          return

      # Get the color of the pixel at the plant's position
      pixel_color = self.viewport.get_at((int(self.position[0]), int(self.position[1])))
      # Check if the pixel is blue (representing water)
      if pixel_color == GREEN:
          # If the pixel is blue, increase the plant's growth
          self.growth += self.growth_rate
      else:
          # If the pixel is not blue, decrease the plant's growth
          self.growth -= self.growth_rate
    
    def draw(self):
        # Draw the plant at its current position within the viewport
        pygame.draw.circle(self.viewport, GREEN, self.position, int(self.growth))
