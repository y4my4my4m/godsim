import random
from family import Family

class Player:
  def __init__(self, world, game_viewport):
    self.world = world
    self.game_viewport = game_viewport

  def create_family(self):
    region = random.choice(self.world.regions)
    family = Family(self.world, region, self.game_viewport)
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
    family = Family(self.world, region, self.game_viewport)
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
