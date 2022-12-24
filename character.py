import pygame
import random
from variables import GREEN, RED

class Character:
  def __init__(self, family, position, screen, world, sprite):
    self.family = family
    self.family.characters.append(self)
    self.hunger = 0
    self.thirst = 0
    self.faith = 0
    self.age = 0
    self.position = position
    self.alive = True
    self.death_timer = 0
    self.sprite = sprite
    self.screen = screen
    self.rect = pygame.Rect(self.position[0], self.position[1], 4, 4)
    self.world = world

  def draw(self):
    # Set the color of the character based on whether they are alive or dead
    if self.alive:
      self.screen.blit(self.sprite, self.position)
    else:
      pygame.draw.circle(self.screen, RED, self.position, 4)

  def update(self):
    self.hunger += 0.1
    self.thirst += 0.1
    self.age += 0.1
    self.faith -= 0.1
  
    if self.hunger >= 100:
      self.die()
    if self.thirst >= 100:
      self.die()

    # # Calculate the bias based on faith, hunger, and thirst
    # bias = self.calculate_bias(self.faith, self.hunger, self.thirst)

    # Add a new character randomly
    if random.random() < 0.001:
      self.family.add_character()

  def die(self):
    self.alive = False
    # Update the death timer
    self.death_timer += 1
    # If the death timer has reached a certain threshold, remove the character from the family
    if self.death_timer >= 60:  # 60 is the threshold in this example
      try:
          self.family.characters.remove(self)
          if len(self.family.characters) == 0:
            self.world.families.remove(self.family)
      except ValueError:
          pass  # Character has already been removed from the list
    
  def eat(self, food):
    self.hunger -= food

  def drink(self, water):
    self.thirst -= water
    
  def worship(self, faith):
    self.faith += faith

  def calculate_bias(self, faith, hunger, thirst):
    bias = faith + (100 - hunger) + (100 - thirst)
    return bias