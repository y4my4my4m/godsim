from PIL import Image
import glob
import os
import random
import pygame

# Set the root directory for the sprites
root_dir = "sprites/characters"

# Get a list of all the subdirectories (i.e., character directories)
character_dirs = [os.path.join(root_dir, d) for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]

class SingleSprite:
  def __init__(self):
    self.x = 0
    self.y = 0
    # Load all the idle frames for the selected character
    self.idle_frames = []
    self.walk_frames = []

    # Select a random character directory
    self.character_dir = random.choice(character_dirs)

    # print(glob.glob(os.path.join(self.character_dir, "*Idle_*.png")))
    for filepath in glob.glob(os.path.join(self.character_dir, "*Idle_*.png")):
        frame = pygame.image.load(filepath)
        self.idle_frames.append(frame)
    for filepath in glob.glob(os.path.join(self.character_dir, "*Walk_*.png")):
        frame = pygame.image.load(filepath)
        self.walk_frames.append(frame)