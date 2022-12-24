import pygame

class Wheat(pygame.sprite.Sprite):
    def __init__(self, position, speed, world):
        super().__init__()
        self.position = list(position)
        self.speed = speed
        # Load the wheat image and get its dimensions
        self.image = pygame.image.load("sprites/wheat.png")
        # self.image = pygame.transform.scale(self.image, (16, 16))
        self.width, self.height = self.image.get_size()
        # Create a rect object using the dimensions of the image
        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        self.world = world

    def update(self):
        self.position[1] += self.speed
        # Update the rect object to reflect the new position of the wheat
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

        for family in self.world.families:
          # for character in family.characters:
          for character in family.characters:
            if self.rect.colliderect(character.rect):
              print("hit")
              # Check if the member is hungry
              if character.hunger > 0:
                  # Feed the member and decrease their hunger
                  character.hunger -= 5
                  # Decrease the player's wheat by the amount used to feed the member
                  self.world.resources['food'] -= 5
                  self.kill()

    def draw(self, surface):
        # Draw the wheat image on the surface at the current position
        surface.blit(self.image, self.position)