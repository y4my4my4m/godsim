import pygame
from variables import GREEN, RED

class Character:
  def __init__(self, family, position, sprite):
    self.family = family
    self.family.characters.append(self)
    self.hunger = 0
    self.thirst = 0
    self.age = 0
    self.faith = 0
    self.position = position
    self.alive = True
    self.death_timer = 0
    self.sprite = sprite

  def draw(self, screen, game_viewport):
    # Set the color of the character based on whether they are alive or dead
    if self.alive:
      color = GREEN
    else:
      color = RED

    # Draw the character
    # pygame.draw.circle(screen, color, self.position, 5)
    screen.blit(self.sprite, self.position)

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
    self.alive = False
    # Update the death timer
    self.death_timer += 1
    # If the death timer has reached a certain threshold, remove the character from the family
    if self.death_timer >= 60:  # 60 is the threshold in this example
      try:
          self.family.characters.remove(self)
      except ValueError:
          pass  # Character has already been removed from the list
    
  def eat(self, food):
    self.hunger -= food
    
  def drink(self, water):
    self.thirst -= water
    
  def worship(self, faith):
    self.faith += faith