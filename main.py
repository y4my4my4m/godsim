import random

class World:
  def __init__(self):
    self.characters = []
    self.resources = {"food": 100, "water": 100, "faith": 0}
    self.regions = []
  
  def update(self):
    for character in self.characters:
      character.update()
      
    # Random events
    if random.random() < 0.1:
      self.resources["food"] += 10
      print("A bountiful harvest has increased the food supply by 10!")
    if random.random() < 0.1:
      self.resources["faith"] += 10
      print("A religious event has increased the faith of the people by 10!")
      
  def add_character(self, character):
    self.characters.append(character)
    character.region = self.regions[0]

class Character:
  def __init__(self, world):
    self.world = world
    self.hunger = 0
    self.thirst = 0
    self.age = 0
    self.faith = 0
    self.region = None
    
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
    self.world.characters.remove(self)
    
  def eat(self, food):
    self.hunger -= food
    
  def drink(self, water):
    self.thirst -= water

  def worship(self, faith):
    self.faith += faith

class Player:
  def __init__(self, world):
    self.world = world
    
  def create_character(self):
    character = Character(self.world)
    self.world.add_character(character)
    
  def feed_character(self, character, food):
    if self.world.resources["food"] >= food:
      character.eat(food)
      self.world.resources["food"] -= food
        
  def give_water_to_character(self, character, water):
    if self.world.resources["water"] >= water:
      character.drink(water)
      self.world.resources["water"] -= water
      
  def inspire_faith(self, character, faith):
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

  print("Characters:")
  for character in world.characters:
    print("  Hunger:", character.hunger)
    print("  Thirst:", character.thirst)
    print("  Age:", character.age)
    print("  Faith:", character.faith)
    print("  Region:", character.region.name)
    print("  ------------------")
    
  # Let the player take an action
  action = input("What do you want to do? (create/feed/water/faith) ")
  if action == "create":
    player.create_character()
  elif action == "feed":
    character_index = int(input("Which character do you want to feed? (Enter the character's index) "))
    food = int(input("How much food do you want to give? "))
    player.feed_character(world.characters[character_index], food)
  elif action == "water":
    character_index = int(input("Which character do you want to give water to? (Enter the character's index) "))
    water = int(input("How much water do you want to give? "))
    player.give_water_to_character(world.characters[character_index], water)
  elif action == "faith":
    character_index = int(input("Which character do you want to inspire? (Enter the character's index) "))
    faith = int(input("How much faith do you want to inspire? "))
    player.inspire_faith(world.characters[character_index], faith)
  else:
    print("Invalid action")