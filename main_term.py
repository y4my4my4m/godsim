import random

class World:
  def __init__(self):
    self.families = []
    self.resources = {"food": 100, "water": 100, "faith": 0}
    self.regions = []
  
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
      
  def add_family(self, family):
    self.families.append(family)

class Family:
  def __init__(self, world, region):
    self.world = world
    self.region = region
    self.characters = []
    
    # Add at least 2 characters
    for i in range(2):
      self.add_character()
    
  def update(self):
    for character in self.characters:
      character.update()
      
    # Add a new character randomly
    if random.random() < 0.1:
      self.add_character()
      
  def add_character(self):
    character = Character(self)
    self.characters.append(character)

class Region:
  def __init__(self, name):
    self.name = name

class Character:
  def __init__(self, family):
    self.family = family
    self.hunger = 0
    self.thirst = 0
    self.age = 0
    self.faith = 0
    
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

class Player:
  def __init__(self, world):
    self.world = world
    
  def create_family(self):
    region = random.choice(self.world.regions)
    family = Family(self.world, region)
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
    for character in family.characters:
      character.worship(faith)
    self.world.resources["faith"] += faith


# Create a new world and player
world = World()
player = Player(world)

# Create some regions
world.regions.append(Region("Desert"))
world.regions.append(Region("Jungle"))
world.regions.append(Region("Mountains"))

# Main game loop
while True:
  # Update the world
  world.update()
  
  # Print the current state of the world
  print("Resources:")
  print("  Food:", world.resources["food"])
  print("  Water:", world.resources["water"])
  print("  Faith:", world.resources["faith"])
  print("Families:")
  for i, family in enumerate(world.families):
    print(f"  Family {i}:")
    print("    Region:", family.region.name)
    print("    Characters:")
    for j, character in enumerate(family.characters):
      print(f"      Character {j}:")
      print("        Hunger:", character.hunger)
      print("        Thirst:", character.thirst)
      print("        Age:", character.age)
      print("        Faith:", character.faith)
      
  # Let the player take an action
  action = input("What do you want to do? (create/feed/water/faith) ")
  if action == "create":
    player.create_family()
  elif action == "feed":
    family_index = int(input("Which family do you want to feed? (Enter the family's index) "))
    food = int(input("How much food do you want to give? "))
    player.feed_family(world.families[family_index], food)
  elif action == "water":
    family_index = int(input("Which family do you want to give water to? (Enter the family's index) "))
    water = int(input("How much water do you want to give? "))
    player.give_water_to_family(world.families[family_index], water)
  elif action == "faith":
    family_index = int(input("Which family do you want to inspire? (Enter the family's index) "))
    faith = int(input("How much faith do you want to inspire? "))
    player.inspire_faith(world.families[family_index], faith)
  else:
    print("Invalid action")