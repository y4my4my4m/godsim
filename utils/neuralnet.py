import pygame
import torch
import csv
import random

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

        # Convert the label to a PyTorch tensor
        label = torch.tensor([float(label)])
        # Extract the sprite from the spritesheet using the coordinates
        sprite = spritesheet.subsurface(pygame.Rect(int(row[1]), int(row[2]), int(row[3]), int(row[4])))
        # Scale down the sprite to 4x4 pixels
        sprite = pygame.transform.scale(sprite, (4, 4))
        # Convert the sprite to a PyTorch tensor
        sprite_tensor = torch.from_numpy(pygame.surfarray.array3d(sprite))
        # Add the sprite tensor and label to the training data
        training_data.append((sprite_tensor, label))


inputs = [x[0] for x in training_data]
labels = [x[1] for x in training_data]
inputs = torch.stack(inputs)
labels = torch.tensor(labels, dtype=torch.float32)
# Convert the training data to a PyTorch tensor
training_data = torch.stack(training_data)

# Create a neural network
model = torch.nn.Sequential(
    torch.nn.Linear(4*4*3, 32),
    torch.nn.ReLU(),
    torch.nn.Linear(32, 1),
)

# Set the loss function and optimizer
loss_fn = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters())

# Train the model
for i in range(1000):
   # Shuffle the training data
   random.shuffle(training_data)
   # Split the training data into inputs and labels
   inputs = [x[0] for x in training_data]
   labels = [x[1] for x in training_data]
   for input, label in zip(inputs, labels):
    # Clear the gradients
    optimizer.zero_grad()
    # Compute the model's output
    output = model(input)
    # Compute the loss
    loss = loss_fn(output, label)
    # Backpropagate the gradients
    loss.backward()
    # Update the model's parameters
    optimizer.step()


for sprite in sprites:
    # Resize the sprite to 4x4 pixels
    sprite = pygame.transform.scale(sprite, (4, 4))
    # Convert the sprite to a list of pixel values
    sprite_data = list(pygame.surfarray.array2d(sprite).flatten())
    # Predict the label for the sprite
    prediction = model.predict([sprite_data])[0]
    # Draw the sprite on the screen
    screen.blit(sprite, (prediction * 5, 0))
    # Update the display
    pygame.display.update()