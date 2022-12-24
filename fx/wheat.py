import pygame

class Wheat(pygame.sprite.Sprite):
    def __init__(self, position, speed):
        super().__init__()
        self.position = list(position)
        self.speed = speed
        # Load the wheat image and get its dimensions
        self.image = pygame.image.load("sprites/wheat.png")
        # self.image = pygame.transform.scale(self.image, (16, 16))
        self.width, self.height = self.image.get_size()
        # Create a rect object using the dimensions of the image
        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)

    def update(self):
        self.position[1] += self.speed
        # Update the rect object to reflect the new position of the wheat
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    def draw(self, surface):
        # Draw the wheat image on the surface at the current position
        surface.blit(self.image, self.position)