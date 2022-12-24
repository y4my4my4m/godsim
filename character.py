import pygame
from variables import GREEN, RED

class Character:
  def __init__(self, family, position):
    self.family = family
    self.family.characters.append(self)
    self.hunger = 0
    self.thirst = 0
    self.age = 0
    self.faith = 0
    self.position = position
    self.alive = True

  def draw(self, screen, game_viewport):
    # Set the color of the character based on whether they are alive or dead
    if self.alive:
      color = GREEN
    else:
      color = RED

    # Draw the character
    pygame.draw.circle(screen, color, self.position, 5)

  def update(self):
    self.hunger += 1
    self.thirst += 1
    self.age += 1
    self.faith -= 1
    
    if self.hunger >= 100:
      self.die()
    if self.thirst >= 100:
      self.die()

  def die(self):
    self.family.characters.remove(self)
    
  def eat(self, food):
    self.hunger -= food
    
  def drink(self, water):
    self.thirst -= water
    
  def worship(self, faith):
    self.faith += faith