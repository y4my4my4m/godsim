import pygame
import os
from PIL import Image
class SingleSprite:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.sprites = []
    self.path = "sprites/characters/"

  def create_sprites(self):
    for file in os.listdir(self.path):
      if file.endswith(".png"):
        # sprite = Image.open(os.path.join(self.path, file))
        sprite = pygame.image.load(self.path+file)
        # self.sprites.append(sprite_sheet)
            
        sprite_rect = pygame.Rect(0,0,32,32)
        # print(sprite_rect)
        sprite = sprite.subsurface(sprite_rect)
        sprite = pygame.transform.scale(sprite, (32, 32))
        # Add the sprite
        self.sprites.append(sprite)