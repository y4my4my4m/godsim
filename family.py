import random
from character import Character

THRESHOLD = 50  # The maximum distance at which the characters should move towards each other
STEP = 5  # The amount by which the characters should move towards each other

class Family:
  def __init__(self, world, region, game_viewport):
    self.world = world
    self.region = region
    self.characters = []
    self.game_viewport = game_viewport
    
    # Add at least 2
    for i in range(2):
      self.add_character()

  def update(self):
    # Calculate the average position of the family members
    x_total = 10
    y_total = 10
    for character in self.characters:
      x_total += character.position[0]
      y_total += character.position[1]
      x_avg = x_total / len(self.characters)
      y_avg = y_total / len(self.characters)
    
    # Add a small random displacement to the average position
    displacement = 10
    x_avg += random.uniform(-displacement, displacement)
    y_avg += random.uniform(-displacement, displacement)
    # Move each character towards the average position if it is far enough away
    for character in self.characters:
        distance = ((character.position[0] - x_avg) ** 2 + (character.position[1] - y_avg) ** 2) ** 0.5
        if distance > THRESHOLD:
            character.position = (
                character.position[0] + (x_avg - character.position[0]) * STEP / distance,
                character.position[1] + (y_avg - character.position[1]) * STEP / distance
            )
        character.update()

    # Add a new character randomly
    if random.random() < 0.1:
      self.add_character()
        
  def add_character(self):
    # Check if the family has any characters
    if len(self.characters) == 0:
      # If the family has no characters, just add the new character at a random position
      x_pos = random.uniform(self.game_viewport.x, self.game_viewport.w)
      y_pos = random.uniform(self.game_viewport.y, self.game_viewport.h)
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
