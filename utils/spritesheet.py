import pygame
import csv
class Spritesheet:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.sprites = []
    self.spritesheet = pygame.image.load("sprites/spritesheet.png")

  def create_sprites(self):
    # Open the sprites.txt file
    with open("sprites/sprites.txt") as f:
        # Read the contents of the file using the csv reader
        reader = csv.reader(f, delimiter=",")
        # Iterate through the list of lines
        for i, row in enumerate(reader):
          if i >= 4:
            return
          # Split the line into a list of coordinates
          y, x, w, h = map(int, row[1:])
          print(x,y,w,h)
          sprite_rect = pygame.Rect(x,y,4,4)
          # print(sprite_rect)
          sprite = self.spritesheet.subsurface(sprite_rect)

          # sprite = self.spritesheet.subsurface(pygame.Rect(x,y,w,h))
          # Extract the sprite from the spritesheet using the coordinates
          # sprite = self.spritesheet.subsurface(pygame.Rect(x, y, w - x, h - y))
          # Scale down the sprite to 4x4 pixels
          sprite = pygame.transform.scale(sprite, (32, 32))
          # Add the sprite
          self.sprites.append(sprite)