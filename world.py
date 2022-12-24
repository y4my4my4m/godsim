import pygame
import random
from variables import BLACK, WHITE, RED, GREEN, BLUE
from fx.plant import Plant
from fx.raindrop import Raindrop

class World:
  
  def __init__(self, game_viewport, screen):
    self.families = []
    self.resources = {"food": 100, "water": 100, "faith": 0}
    self.regions = []
    self.game_viewport = game_viewport
    self.screen = screen
    self.raindrops = []   # Create a list to store the raindrops
    self.plants = []      # Create a list to store the plants

    # Set the update rate for the plant in frames per second
    self.plant_update_frequency = 6500  # update plant every 60 updates
    self.update_counter = 0

    # Generate a random starting position for the raindrops
    for i in range(200):
        x = random.uniform(self.game_viewport.x, self.game_viewport.x + self.game_viewport.w)
        y = random.uniform(self.game_viewport.y, self.game_viewport.y + self.game_viewport.h)
        raindrop = Raindrop((x,y), game_viewport)
        self.add_raindrop(raindrop)

    for h in range(200):
        x = random.uniform(self.game_viewport.x, self.game_viewport.x + self.game_viewport.w)
        y = random.uniform(self.game_viewport.y, self.game_viewport.y + self.game_viewport.h)
        plant = Plant((x,y), screen)
        self.add_plant(plant)
              
  def update(self):
    
    self.update_counter += 1
    # Update the families
    for family in self.families:
      family.update()
    
    # Update the plants
    # if self.update_counter % (60 / self.plant_update_frequency) == 0:
    for plant in self.plants:
      plant.update()

    # Update the raindrops
    # for raindrop in self.raindrops:
    #   raindrop.update()

    # Random events
    if random.random() < 0.1:
      self.resources["food"] += 10
      print("A bountiful harvest has increased the food supply by 10!")
    if random.random() < 0.1:
      self.resources["faith"] += 10
      print("A religious event has increased the faith of the people by 10!")


  def draw(self, screen):
    # Draw the characters
    for family in self.families:
      for character in family.characters:
        character.draw(screen, self.game_viewport)
      for i in range(len(family.characters) - 1):
        character1 = family.characters[i]
        character2 = family.characters[i + 1]
        pygame.draw.line(screen, WHITE, character1.position, character2.position)

    for plant in self.plants:
        plant.draw()

    # for raindrop in self.raindrops:
    #     raindrop.draw(screen)

  def add_family(self, family):
    self.families.append(family)

  def add_plant(self, plant):
      self.plants.append(plant)

  def add_raindrop(self, raindrop):
      self.raindrops.append(raindrop)