import pygame
import time
from variables import BLACK, WHITE, RED, GREEN
from world import World
# from character import Character
from player import Player
# from family import Family
from region import Region

# Initialize Pygame
pygame.init()

# Load the font
font = pygame.font.Font(None, 18)

# Set the window size and title
window_size = (800, 600)
window_title = "God Sim"
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)
# Set the frame rate
clock = pygame.time.Clock()
frame_rate = 60

# Define the game viewport as a rectangle with a width of 600 and a height of 400, starting at an x-coordinate of 100
game_viewport = pygame.Rect(205, 100, 580, 400)

# Create the input field for the family index
family_index_input_field = pygame.draw.rect(screen, WHITE, (200, 180, 50, 30))
text = font.render("Family index:", True, BLACK)
screen.blit(text, (205, 185))

# Create the world
world = World(game_viewport, screen)

# Add some regions
world.regions.append(Region("Desert"))
world.regions.append(Region("Forest"))
world.regions.append(Region("Mountains"))

# Create the player
player = Player(world, screen, game_viewport)

# Action selection
holding_wheat = False
holding_water = False
holding_holy = False

# Set the wheat spawn rate (in seconds)
wheat_spawn_rate = 0.1
water_spawn_rate = 0.1
holy_spawn_rate = 0.1

# Set the last time the wheat was spawned
last_wheat_spawn_time = 0
last_water_spawn_time = 0
last_holy_spawn_time = 0

# Set the wheat speed
wheat_speed = 1
water_speed = 1
holy_speed = 1

# Main game loop
running = True
while running:
  # Get the cursor position
  cursor_pos = pygame.mouse.get_pos()
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
        # Set the cursor to the hand with wheat image
        pygame.mouse.set_cursor(*pygame.cursors.broken_x)
        # Set a flag to indicate that the player is holding wheat
        player.isHoldingWheat = True
        break
      # Check if the give water to family button was clicked
      elif give_water_to_family_button.collidepoint(event.pos):
        pygame.mouse.set_cursor(*pygame.cursors.broken_x)
        player.isHoldingWater = True
        break
      # Check if the inspire faith button was clicked
      elif inspire_faith_button.collidepoint(event.pos):
        pygame.mouse.set_cursor(*pygame.cursors.broken_x)
        player.isHoldingHoly = True
        break
    elif event.type == pygame.MOUSEBUTTONUP:
        # Check if the player was holding wheat
        if player.isHoldingWheat:
            # Reset the cursor to the default image
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            # Reset the holding wheat flag
            player.isHoldingWheat = False
        # Check if the player was holding water
        if player.isHoldingWater:
            # Reset the cursor to the default image
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            # Reset the holding water flag
            player.isHoldingWater = False
        # Check if the player was holding holy
        if player.isHoldingHoly:
            # Reset the cursor to the default image
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            # Reset the holding holy flag
            player.isHoldingHoly = False
  # Draw the world
  screen.fill(BLACK)

  # Draw the viewport container
  pygame.draw.rect(screen, (40,40,40), game_viewport)

  # Update the world
  world.update()

  # Check if the mouse button is down and it's time to spawn a new Wheat
  if player.isHoldingWheat and time.time() - last_wheat_spawn_time >= wheat_spawn_rate:
      # Create a new Wheat sprite at the mouse position
      player.create_weath(cursor_pos)
      # Update the last wheat spawn time
      last_wheat_spawn_time = time.time()

  for wheat in player.wheat_group:
    wheat.update()
    wheat.draw(screen)

  # Check if the mouse button is down and it's time to spawn a new Water
  if player.isHoldingWater and time.time() - last_water_spawn_time >= water_spawn_rate:
      # Create a new water sprite at the mouse position
      player.create_water(cursor_pos)
      # Update the last water spawn time
      last_water_spawn_time = time.time()

  for water in player.water_group:
    water.update()
    water.draw(screen)

  # Check if the mouse button is down and it's time to spawn a new Holy
  if player.isHoldingHoly and time.time() - last_holy_spawn_time >= holy_spawn_rate:
      # Create a new holy sprite at the mouse position
      player.create_holy(cursor_pos)
      # Update the last holy spawn time
      last_holy_spawn_time = time.time()

  for holy in player.holy_group:
    holy.update()
    holy.draw(screen)

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
    text = font.render(f"{len(family.characters)}: {family.name}", True, WHITE)
    screen.blit(text, (window_size[0] - 150, y))

    # Create rectangles to represent the hunger, thirst, and faith bars
    hunger_rect = pygame.Rect(window_size[0] - 150, y + 14, (family.hunger_avg * 10)/10, 2)
    thirst_rect = pygame.Rect(window_size[0] - 150, y + 18, (family.thirst_avg * 10)/10, 2)
    faith_rect = pygame.Rect(window_size[0] - 150, y + 22, (family.faith_avg * 10)/10, 2)
    # Draw the rectangles on the screen, positioning them below the family
    pygame.draw.rect(screen, (200, 20, 50), hunger_rect)
    pygame.draw.rect(screen, (20, 200, 50), thirst_rect)
    pygame.draw.rect(screen, (50, 20, 200), faith_rect)
    y += 25
  
  # Update the display
  pygame.display.flip()
  
  # Delay for 1 second
  # pygame.time.delay(20)

  # Limit the frame rate
  clock.tick(frame_rate)


# Quit Pygame
pygame.quit()
