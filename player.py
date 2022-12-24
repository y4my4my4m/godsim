import random
import pygame
from family import Family
from fx.wheat import Wheat
class Player:
  def __init__(self, world, screen, game_viewport):
    self.world = world
    self.screen = screen
    self.game_viewport = game_viewport
    self.isHoldingWheat = False
    # Create a sprite group for the Wheat objects
    self.wheat_group = pygame.sprite.Group()

  def create_family(self):
    region = random.choice(self.world.regions)
    family = Family(self.world, region, self.screen, self.game_viewport)
    self.world.add_family(family)
    
  def feed_family(self, family, food):
    if self.world.resources["food"] >= food:
      for character in family.characters:
        character.eat(food)
      self.world.resources["food"] -= food
      
  def give_water_to_family(self, family, water):
    if self.world.resources["water"] >= water:
      for character in family.characters:
        character.drink(water)
      self.world.resources["water"] -= water
      
  def inspire_faith(self, family, faith):
    if self.world.resources["faith"] >= faith:
      for character in family.characters:
        character.worship(faith)
      self.world.resources["faith"] -= faith

  def create_family(self):
    region = random.choice(self.world.regions)
    family = Family(self.world, region, self.screen, self.game_viewport)
    self.world.add_family(family)
    
  def feed_family(self, family, food):
    if self.world.resources["food"] >= food:
      for character in family.characters:
        character.eat(food)
      self.world.resources["food"] -= food
      
  def give_water_to_family(self, family, water):
    if self.world.resources["water"] >= water:
      for character in family.characters:
        character.drink(water)
      self.world.resources["water"] -= water
      
  def inspire_faith(self, family, faith):
    if self.world.resources["faith"] >= faith:
      for character in family.characters:
        character.worship(faith)
      self.world.resources["faith"] -= faith

  def create_weath(self, cursor_pos):
      # Check if the player is holding wheat
      if self.isHoldingWheat:
        # Create a Wheat object and add it to the sprite group
        wheat = Wheat(cursor_pos, 5)
        self.wheat_group.add(wheat)

          # # Iterate through the family members
          # for member in self.world.families[0].characters:
          #     # Check if the member is hungry
          #     if member.hunger > 0:
          #         # Feed the member and decrease their hunger
          #         member.hunger -= 5
          #         # Decrease the player's wheat by the amount used to feed the member
          #         self.world.resources['food'] -= 5
