import pygame
import random
from variables import GREEN, RED
from utils.singlesprites import SingleSprite
class Character:
  def __init__(self, family, position, screen, world):
    self.family = family
    self.family.characters.append(self)
    self.hunger = 0
    self.thirst = 0
    self.faith = 0
    self.age = 0
    self.position = position
    self.alive = True
    self.death_timer = 0
    self.screen = screen
    self.rect = pygame.Rect(self.position[0], self.position[1], 4, 4)
    self.world = world
    self.path = "sprites/characters/"
    # Create the idle sprites using the SingleSprite class
    single_sprite = SingleSprite()
    self.idle_frames = single_sprite.idle_frames
    self.walk_frames = single_sprite.walk_frames
    self.frame_rate = 10
    self.timer = 0
    self.current_frame = 0
    self.state = "idle"
    self.animation_frames = self.idle_frames

  def get_state(self):
    # Check the character's state and choose the appropriate animation frames
    if self.state == "idle":
        self.animation_frames = self.idle_frames
    elif self.state == "walking":
        self.animation_frames = self.walk_frames


  def animate(self):
    # Increment the timer
    self.timer += 1
    # Check if it's time to switch frames
    if len(self.idle_frames) > 0:
      if self.timer % (self.frame_rate // len(self.idle_frames)) == 0:
          # Reset the timer
          self.timer = 0
          # Increment the current frame index
          self.current_frame += 1
          if self.current_frame >= len(self.idle_frames):
              self.current_frame = 0
    else:
      self.frame_rate = 10


  def draw(self):
    # Set the color of the character based on whether they are alive or dead
    if self.alive:
      self.animate()
      if self.idle_frames:
        self.screen.blit(self.animation_frames[self.current_frame], self.position)
      # self.screen.blit(self.sprite, self.position)
    else:
      pygame.draw.circle(self.screen, RED, self.position, 4)

  def update(self):
    self.hunger += 0.1
    self.thirst += 0.1
    self.age += 0.1
    self.faith -= 0.1
  
    if self.hunger >= 100:
      self.die()
    if self.thirst >= 100:
      self.die()

    # # Calculate the bias based on faith, hunger, and thirst
    # bias = self.calculate_bias(self.faith, self.hunger, self.thirst)

    # Add a new character randomly
    if random.random() < 0.001:
      self.family.add_character()

  def die(self):
    self.alive = False
    # Update the death timer
    self.death_timer += 1
    # If the death timer has reached a certain threshold, remove the character from the family
    if self.death_timer >= 60:  # 60 is the threshold in this example
      try:
          self.family.characters.remove(self)
          if len(self.family.characters) == 0:
            self.world.families.remove(self.family)
      except ValueError:
          pass  # Character has already been removed from the list
    
  def eat(self, food):
    self.hunger -= food

  def drink(self, water):
    self.thirst -= water
    
  def worship(self, faith):
    self.faith += faith

  def calculate_bias(self, faith, hunger, thirst):
    bias = faith + (100 - hunger) + (100 - thirst)
    return bias