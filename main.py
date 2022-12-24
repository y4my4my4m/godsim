import pygame
import random
from variables import BLACK, WHITE, RED, GREEN
from world import World
from character import Character
from player import Player
from family import Family

# Initialize Pygame
pygame.init()

# Load the font
font = pygame.font.Font(None, 20)

# Set the window size and title
window_size = (800, 400)
window_title = "God Sim"
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)

# Define the game viewport as a rectangle with a width of 600 and a height of 400, starting at an x-coordinate of 100
game_viewport = pygame.Rect(100, 0, 600, 400)

# Create the input field for the family index
family_index_input_field = pygame.draw.rect(screen, WHITE, (200, 180, 50, 30))
text = font.render("Family index:", True, BLACK)
screen.blit(text, (205, 185))
class Region:
  def __init__(self, name):
    self.name = name

# Create the world
world = World(game_viewport)

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
