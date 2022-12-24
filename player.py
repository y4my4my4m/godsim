import random
import pygame
from family import Family
from fx.wheat import Wheat
from fx.water import Water
from fx.holy import Holy
class Player:
  def __init__(self, world, screen, game_viewport):
    self.world = world
    self.screen = screen
    self.game_viewport = game_viewport
    self.isHoldingWheat = False
    self.isHoldingWater = False
    self.isHoldingHoly = False
    # Create a sprite group for the Wheat objects
    self.wheat_group = pygame.sprite.Group()
    self.water_group = pygame.sprite.Group()
    self.holy_group = pygame.sprite.Group()

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

  def create_weath(self, cursor_pos):
      # Check if the player is holding wheat
      if self.isHoldingWheat and self.world.resources['food'] > 0:
        # Create a Wheat object and add it to the sprite group
        wheat = Wheat(cursor_pos, 5, self)
        self.wheat_group.add(wheat)

  def create_water(self, cursor_pos):
      # Check if the player is holding wheat
      if self.isHoldingWater and self.world.resources['water'] > 0:
        # Create a Water object and add it to the sprite group
        water = Water(cursor_pos, 5, self)
        self.water_group.add(water)

  def create_holy(self, cursor_pos):
      # Check if the player is holding wheat
      if self.isHoldingHoly and self.world.resources['faith'] > 0:
        # Create a Holy object and add it to the sprite group
        holy = Holy(cursor_pos, 5, self)
        self.holy_group.add(holy)