import pygame
import torch
from neuralnet import NeuralNet
import csv
import random

# This is a neuralnet that takes sprites from a spritesheet and creates new sprites
# Initialize Pygame
pygame.init()
# Set the window size and title
window_size = (800, 600)
window_title = "God Sim - NeuralNet"
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)
# Load the spritesheet image
spritesheet = pygame.image.load("sprites/spritesheet.png")
# Initialize an empty list to store the training data
training_data = []
sprites = []

# Open the sprites.txt file
with open("sprites/sprites.txt") as f:
    # Read the contents of the file into a list of lines
    reader = csv.reader(f)
    # Iterate through the rows of the CSV
    for row in reader:
        # Split the label and sprite name from the first field
        label = row[0].split(',')
        label = label[0]
        for s in label:
            if s.isdigit():
                label = s
        # Skip if out of bound
        if int(row[1]) > 100 or int(row[2]) > 100:
            continue
        # Convert the label to a PyTorch tensor
        label = torch.tensor([float(label)])
        # Extract the sprite from the spritesheet using the coordinates
        sprite = spritesheet.subsurface(pygame.Rect(int(row[1]), int(row[2]), int(row[3]), int(row[4])))
        # Scale down the sprite to 4x4 pixels
        sprite = pygame.transform.scale(sprite, (4, 4))
        sprites.append(sprite)
        # Convert the sprite to a PyTorch tensor
        sprite_tensor = torch.from_numpy(pygame.surfarray.array3d(sprite))
        # Add the sprite tensor and label to the training data
        training_data.append((sprite_tensor, label))

# Convert the training data to a PyTorch tensor
training_data = [(torch.tensor(x[0]), torch.tensor(x[1])) for x in training_data]

# Create a neural network
model = NeuralNet()

# Set the loss function and optimizer
loss_fn = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters())

# Set the amount of noise to add to the input sprites
# noise_level = 0.01
# noise = noise_level * torch.ByteTensor(input.shape).random_().to(torch.float32)
# Train the model
for i in range(10):
   # Shuffle the training data
   random.shuffle(training_data)
   inputs = [x[0] for x in training_data]
   for input in inputs:
# Convert the input tensor to a float tensor
    input = input.to(torch.float32)
    # Reshape the input tensor to a 1D tensor
    # input = input.view(-1, 4*4*3)
    # Clear the gradients
    optimizer.zero_grad()
    # Compute the model's output
    output = model(input)
    # Update the model's parameters
    optimizer.step()

counter = 0
for sprite in sprites:
    # Resize the sprite to 4x4 pixels
    sprite = pygame.transform.scale(sprite, (4, 4))
    # Convert the sprite to a list of pixel values
    sprite_data = list(pygame.surfarray.array2d(sprite).flatten())
    # Process the sprite through the neural network
    # Reshape the input tensor to a 2D tensor with shape (batch_size, input_size)
    input = torch.tensor(sprite_data).view(-1, 4*4*3)
    output_sprite = model(input)
    # Convert the output sprite back to a Pygame surface
    output_surface = pygame.surfarray.make_surface(output_sprite.detach().numpy().astype)
    # Save the output sprite to a file
    pygame.image.save(output_surface, f"utils/trained/sprite{counter}.png")
    counter += 1
    # Draw the sprite on the screen
    screen.blit(sprite, (output_surface * 5, 0))
    # Update the display
    pygame.display.update()