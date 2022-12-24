import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size and title
window_size = (800, 400)
window_title = "God Sim"
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)

# Define the game viewport as a rectangle with a width of 600 and a height of 400, starting at an x-coordinate of 100
game_viewport = pygame.Rect(100, 0, 600, 400)

# Load the font
font = pygame.font.Font(None, 20)
# Define colors
BLACK = (20, 20, 20)
WHITE = (248, 248, 248)
GREEN = (20, 248, 20)
RED   = (248, 20, 20)

# Create the input field for the family index
family_index_input_field = pygame.draw.rect(screen, WHITE, (200, 180, 50, 30))
text = font.render("Family index:", True, BLACK)
screen.blit(text, (205, 185))

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
            character.draw(screen)
          for i in range(len(family.characters) - 1):
              character1 = family.characters[i]
              character2 = family.characters[i + 1]
              pygame.draw.line(screen, WHITE, character1.position, character2.position)

  def add_family(self, family):
    self.families.append(family)

class Region:
  def __init__(self, name):
    self.name = name
class Family:
  def __init__(self, world, region):
    self.world = world
    self.region = region
    self.characters = []
    
    # Add at least 2
    for i in range(2):
      self.add_character()
    
  def update(self):
    for character in self.characters:
      character.update()
      
    # Add a new character randomly
    if random.random() < 0.1:
      self.add_character()
        
  def add_character(self):
    # Check if the family has any characters
    if len(self.characters) == 0:
      # If the family has no characters, just add the new character at a random position
      x_pos = random.uniform(0, 600)
      y_pos = random.uniform(0, 400)
      character = Character(self, (x_pos, y_pos))
    else:
      # Calculate the average position of the existing family members
      x_total = 0
      y_total = 0
      for character in self.characters:
        x_total += character.position[0]
        y_total += character.position[1]
      x_avg = x_total / len(self.characters)
      y_avg = y_total / len(self.characters)

      # Generate a random position near the average position
      x_pos = x_avg + random.uniform(-50, 50)
      y_pos = y_avg + random.uniform(-50, 50)

      # Create the new character with the random position
      character = Character(self, (x_pos, y_pos))
    self.characters.append(character)



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

  def draw(self, screen):
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
    if self.world.resources["faith"] >= faith:
      for character in family.characters:
        character.worship(faith)
      self.world.resources["faith"] -= faith

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
    if self.world.resources["faith"] >= faith:
      for character in family.characters:
        character.worship(faith)
      self.world.resources["faith"] -= faith

# Create the world
world = World()

# Add some regions
world.regions.append(Region("Desert"))
world.regions.append(Region("Forest"))
world.regions.append(Region("Mountains"))

# Create the player
player = Player(world)

# Main game loop
running = True
while running:
  # Check for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      # Check if the create family button was clicked
      if create_family_button.collidepoint(event.pos):
        player.create_family()
        break
      # Check if the feed family button was clicked
      elif feed_family_button.collidepoint(event.pos):
        family = input("Enter the index of the family you want to feed: ")
        food = input("Enter the amount of food you want to give: ")
        player.feed_family(world.families[family], food)
        break
      # Check if the give water to family button was clicked
      elif give_water_to_family_button.collidepoint(event.pos):
        family = input("Enter the index of the family you want to give water to: ")
        water = input("Enter the amount of water you want to give: ")
        player.give_water_to_family(world.families[family], water)
        break
      # Check if the inspire faith button was clicked
      elif inspire_faith_button.collidepoint(event.pos):
        family = input("Enter the index of the family you want to inspire faith in: ")
        faith = input("Enter the amount of faith you want to give: ")
        player.inspire_faith(world.families[family], faith)
        break
  
  # Draw the world
  screen.fill(BLACK)
  
  # Update the world
  world.update()
  
  # Draw the world
  world.draw(screen)
  
  # Draw the resources
  text = font.render(f"Food: {world.resources['food']}", True, WHITE)
  screen.blit(text, (10, 10))
  text = font.render(f"Water: {world.resources['water']}", True, WHITE)
  screen.blit(text, (10, 50))
  text = font.render(f"Faith: {world.resources['faith']}", True, WHITE)
  screen.blit(text, (10, 90))

  # Draw the buttons
  create_family_button = pygame.draw.rect(screen, WHITE, (10, 130, 180, 40))
  text = font.render("Create a new family", True, BLACK)
  screen.blit(text, (15, 135))
  
  feed_family_button = pygame.draw.rect(screen, WHITE, (10, 180, 180, 40))
  text = font.render("Feed a family", True, BLACK)
  screen.blit(text, (15, 185))
  
  give_water_to_family_button = pygame.draw.rect(screen, WHITE, (10, 230, 180, 40))
  text = font.render("Give water to a family", True, BLACK)
  screen.blit(text, (15, 235))
  
  inspire_faith_button = pygame.draw.rect(screen, WHITE, (10, 280, 180, 40))
  text = font.render("Inspire faith in a family", True, BLACK)
  screen.blit(text, (15, 285))
  
  # Draw the families
  y = 10
  for family in world.families:
    text = font.render(f"Family with {len(family.characters)} characters", True, WHITE)
    screen.blit(text, (window_size[0] - 200, y))
    y += 40
  
  # Update the display
  pygame.display.flip()
  
  # Delay for 1 second
  pygame.time.delay(10)

# Quit Pygame
pygame.quit()
