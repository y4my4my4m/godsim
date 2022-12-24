import pygame
import random
import colorsys
from variables import GREEN, BLUE

def r(a,b):
  return random.randint(a,b)
class Plant:
    def __init__(self, position, viewport):
        self.position = position
        self.viewport = viewport
        self.growth = 0
        self.max_growth = 12
        self.growth_rate = 5
        self.plant_color = GREEN
        self.counter = 0

    def update(self):
      # Check if the plant is fully grown
      if self.growth >= self.max_growth:
          return

      # Increment the counter
      self.counter += 1
      # Check if the counter has reached the desired rate at which plants are created
      if self.counter % 60 == 0:  # This will create a plant every 60 frames
        # Define the base hue for the plant pixels
        base_hue = 120  # green hue
        # Draw the plant
        # rx = random.randint(-self.growth, self.growth)
        # ry = random.randint(-self.growth, self.growth)
        # x = int(self.position[0]) + rx
        # y = int(self.position[1]) + ry
        # Calculate the hue for the pixel
        # hue = base_hue + (rx + ry)
        hue = base_hue
        # Convert the hue to a RGB color
        self.plant_color = tuple(int(c * 255) for c in colorsys.hsv_to_rgb(hue / 360, 1, 1))
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

      # Draw the plant
      # # Round the position to the nearest integer
      # rounded_position = (round(self.position[0]), round(self.position[1]))
      # # # Set the pixel at the rounded position to the plant color
      # self.viewport.set_at(rounded_position, self.plant_color)
      # self.viewport.set_at((round(self.position[0]) + 1, round(self.position[1])), self.plant_color)
      # self.viewport.set_at((round(self.position[0]) - 1, round(self.position[1])), self.plant_color)
      # self.viewport.set_at((round(self.position[0]), round(self.position[1] + 1)), self.plant_color)
      # self.viewport.set_at((round(self.position[0]), round(self.position[1] - 1)), self.plant_color)
      # # # Draw the pixelated plants and flowers using a loop
      # for i in range(-self.growth, self.growth):
      #   for j in range(-self.growth, self.growth):
      #     # Calculate the position of the pixel
      #     x = self.position[0] + i
      #     y = self.position[1] + j
      # Draw the pixel
      self.viewport.set_at((int(self.position[0]), int(self.position[1])), self.plant_color)