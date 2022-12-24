import pygame

class Holy(pygame.sprite.Sprite):
    def __init__(self, position, speed, player):
        super().__init__()
        self.position = list(position)
        self.speed = speed
        # Load the holy image and get its dimensions
        self.image = pygame.image.load("sprites/holy.png")
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.width, self.height = self.image.get_size()
        # Create a rect object using the dimensions of the image
        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        self.player = player
        self.world = player.world
        self.screen = player.screen

    def update(self):
        self.position[1] += self.speed
        # Update the rect object to reflect the new position of the holy
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        if self.rect.y > self.screen.get_height():
            self.consume()

        for family in self.world.families:
          # for character in family.characters:
          for character in family.characters:
            if self.rect.colliderect(character.rect):
              # Check if the member has faith
              if character.faith > 0:
                  # Feed the member and decrease their faith
                  character.faith -= 1
                  # Decrease the player's holy by the amount used to inspire the member
                  self.world.resources['faith'] -= 1
                  self.consume()

    def draw(self, screen):
        # Draw the holy image on the surface at the current position
        screen.blit(self.image, self.position)

    def consume(self):
        self.player.holy_group.remove(self)
        self.kill()