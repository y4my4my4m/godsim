import pygame
import csv

# # Initialize Pygame
# pygame.init()
# # Set the window size and title
# window_size = (800, 600)
# window_title = "God Sim - Spritesheeter"
# screen = pygame.display.set_mode(window_size)
# pygame.display.set_caption(window_title)

# Load the spritesheet image
spritesheet = pygame.image.load("sprites/spritesheet.png")
sprites = []


class Spritesheet:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.sprites = []

  def create_sprites(self):
    # Open the sprites.txt file
    with open("sprites/sprites.txt") as f:
        # Read the contents of the file into a list of lines
        # lines = f.readlines()
        # Read the contents of the file using the csv reader
        reader = csv.reader(f, delimiter=",")
        # Iterate through the list of lines
        for row in reader:
            # Split the line into a list of coordinates
            x1, y1, x2, y2 = map(int, row[1:])
            print(x1,y1,x2,y2)
            # Extract the sprite from the spritesheet using the coordinates
            sprite = spritesheet.subsurface(pygame.Rect(x1, y1, x2 - x1, y2 - y1))
            # Scale down the sprite to 4x4 pixels
            sprite = pygame.transform.scale(sprite, (32, 32))
            # Add the sprite
            self.sprites.append(sprite)



  # while (True):
  #   for sprite in sprites:
  #     # Draw the sprite on the screen
  #     screen.blit(sprite, (x, y))
  #     # Update the x position for the next sprite
  #     x += 4
  #     # If the x position is at the end of the row, move to the next row
  #     if x >= window_size[0]:
  #         x = 0
  #         y += 4
  #     # Update the display
  #     pygame.display.update()