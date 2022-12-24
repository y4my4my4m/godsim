import pygame
import random
from variables import BLACK, WHITE, RED, GREEN

class World:
  def __init__(self, game_viewport):
    self.families = []
    self.resources = {"food": 100, "water": 100, "faith": 0}
    self.regions = []
    self.game_viewport = game_viewport
          
  def update(self):
    for family in self.families:
      family.update()

    # Random events
    if random.random() < 0.1:
      self.resources["food"] += 10
      print("A bountiful harvest has increased the food supply by 10!")
    if random.random() < 0.1:
      self.resources["faith"] += 10
      print("A religious event has increased the faith of the people by 10!")

    # Move the characters
    for family in self.families:
        # Calculate the average position of the family members
        x_total = 0
        y_total = 0
        for character in family.characters:
            x_total += character.position[0]
            y_total += character.position[1]
            x_avg = x_total / len(family.characters)
            y_avg = y_total / len(family.characters)
        
        # Move each character towards the average position
        for character in family.characters:
            character.position = (
                character.position[0] + (x_avg - character.position[0]) / 10,
                character.position[1] + (y_avg - character.position[1]) / 10
            )

  def draw(self, screen):
    # Draw the characters
    for family in self.families:
      for character in family.characters:
        character.draw(screen, self.game_viewport)
      for i in range(len(family.characters) - 1):
        character1 = family.characters[i]
        character2 = family.characters[i + 1]
        pygame.draw.line(screen, WHITE, character1.position, character2.position, self.game_viewport)

  def add_family(self, family):
    self.families.append(family)