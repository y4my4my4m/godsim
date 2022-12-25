import torch
import torch.nn as nn
from PIL import Image
import os
import numpy as np

num_epochs = 10
# Define the neural network architecture
class SpriteGenerator(nn.Module):
  def __init__(self):
    super(SpriteGenerator, self).__init__()
    self.conv1 = nn.Conv2d(4, 32, kernel_size=3, stride=1, padding=1)
    self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
    self.conv3 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)
    self.fc1 = nn.Linear(128 * 16 * 16, 1024)
    self.fc2 = nn.Linear(1024, 256)
    self.fc3 = nn.Linear(256, 3 * 32 * 32)
  
  def forward(self, x):
    # Convert the input to a float
    x = x.float() / 255.0
    x = x.clamp(0, 1)
    # Reshape the input to have the correct shape and number of channels
    x = x.view(-1, 4, 32, 32)
    # x = x.view(-1, 3, 32, 32)[:, :, :, :3]
    x = self.conv1(x)
    x = nn.ReLU()(x)
    x = self.conv2(x)
    x = nn.ReLU()(x)
    x = self.conv3(x)
    x = nn.ReLU()(x)
    x = x.view(-1, 128 * 16 * 16)
    x = self.fc1(x)
    x = nn.ReLU()(x)
    x = self.fc2(x)
    x = nn.ReLU()(x)
    x = self.fc3(x)
    x = x.view(-1, 4, 32, 32)
    return x

# Instantiate the model
model = SpriteGenerator()

# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

def load_sprite_sheets(sprite_sheet_dir):
  # Load the sprite sheets
  sprite_sheets = []
  for file in os.listdir(sprite_sheet_dir):
    if file.endswith(".png"):
      sprite_sheet = Image.open(os.path.join(sprite_sheet_dir, file))
      sprite_sheets.append(sprite_sheet)
      
  return sprite_sheets

def split_sprite_sheets(sprite_sheets):
  # Set the size and resolution of the individual sprites
  sprite_size = (32, 32)
  sprite_res = (3, 3)
  
  # Initialize a list to store the individual sprites
  sprites = []
  
  # Iterate over the sprite sheets
  for sprite_sheet in sprite_sheets:
    # Get the width and height of the sprite sheet
    sheet_width, sheet_height = sprite_sheet.size
    
    # Calculate the number of sprites in the x and y directions
    num_sprites_x = sheet_width // sprite_size[0]
    num_sprites_y = sheet_height // sprite_size[1]
    
    # Iterate over the sprites in the sprite sheet
    for y in range(num_sprites_y):
      for x in range(num_sprites_x):
        # Extract the sprite from the sprite sheet
        sprite = sprite_sheet.crop((x * sprite_size[0], y * sprite_size[1], (x+1) * sprite_size[0], (y+1) * sprite_size[1]))
        
        # Add the sprite to the list
        sprites.append(sprite)
        
  return sprites

def resize_sprites(sprites, size, res):
  # Set the size and resolution of the sprites
  sprite_size = size
  sprite_res = res
  
  # Initialize a list to store the resized sprites
  resized_sprites = []
  
  # Iterate over the sprites
  for sprite in sprites:
    # Convert the sprite to the RGBA mode
    sprite = sprite.convert("RGBA")
    # Resize the sprite
    sprite = sprite.resize(sprite_size, resample=Image.NEAREST)
    
    # Convert the sprite to a NumPy array
    sprite = np.array(sprite)
    # Add the resized sprite to the list
    resized_sprites.append(sprite)
    
  return resized_sprites

def normalize_sprites(sprites):
  # Set the minimum and maximum pixel values
  min_val = 0
  max_val = 255
  
  # Initialize a list to store the normalized sprites
  normalized_sprites = []
  
  # Iterate over the sprites
  for sprite in sprites:
    # Convert the sprite to a numpy array
    sprite = np.array(sprite)
    # Normalize the pixel values
    sprite = (sprite - min_val) / (max_val - min_val)

    # Convert the normalized sprite back to an Image object
    sprite = Image.fromarray(np.uint8(sprite * 255))

    # Add the normalized sprite to the list
    normalized_sprites.append(sprite)
    
  return normalized_sprites

def load_data():
  # Load the sprite sheets
  sprite_sheets = load_sprite_sheets("sprites/Mage")
  
  # Split the sprite sheets into individual sprites
  sprites = split_sprite_sheets(sprite_sheets)
  
  # Resize the sprites to the desired size and resolution
  sprites = resize_sprites(sprites, size=(32, 32), res=(3, 3))
  
  # Normalize the pixel values
  sprites = normalize_sprites(sprites)

  # Convert the sprites to numpy arrays
  sprites = [np.array(sprite) for sprite in sprites]
  
  # Convert the sprites to tensors
  sprites = [torch.from_numpy(sprite) for sprite in sprites]
  
  # Create the training data
  X_train = sprites
  y_train = [torch.Tensor([i]) for i in range(len(X_train))]
  
  return X_train, y_train

def load_test_data():
  # Load the test sprites
  sprite_sheet_dir = "sprites/Mage"
  sprite_sheets = load_sprite_sheets(sprite_sheet_dir)
  sprites = split_sprite_sheets(sprite_sheets)
  sprites = resize_sprites(sprites, (32, 32), (3, 3))
  
  # Convert the sprites to tensors
  X_test = [torch.from_numpy(np.array(sprite)).unsqueeze(0) for sprite in sprites]
  
  # Make predictions for each image in the test set
  y_preds = []
  for X_test_i in X_test:
      y_pred_i = model(X_test_i)
      y_preds.append(y_pred_i)
      
  # Set the target outputs to the original sprites
  y_test = X_test
  
  return X_test, y_test


# Load the training data
X_train, y_train = load_data()

# Training loop
for epoch in range(num_epochs):
  for i, (X, y) in enumerate(zip(X_train, y_train)):
    # Forward pass
    y_pred = model(X)
    loss = criterion(y_pred, y)

    # Save the generated sprites to image files
    for i, sprite in enumerate(y_pred):
        # # Convert the sprite to a NumPy array
        # Convert the sprite to a NumPy array
        sprite = sprite.detach().numpy()
        # Reshape the array to (4, 32, 32)
        sprite = sprite.reshape(4, 32, 32)
        # Scale the sprite values to the range [0, 255]
        sprite = (sprite * 255).astype(np.uint8)
        # Create an image from the raw data in the NumPy array
        sprite = Image.frombytes("RGBA", (32, 32), sprite.tobytes())
        # Convert the sprite to an image
        # sprite = Image.fromarray(sprite)
        # Save the sprite to an image file
        sprite.save(f"utils/trained/{i}.png")
    
    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    # Print progress
    if i % 100 == 0:
      print(f"Epoch {epoch+1}/{num_epochs}, Step {i+1}/{len(X_train)}, Loss = {loss.item():.4f}")

# Test the model on some new, unseen sprites
X_test, y_test = load_test_data()
y_pred = model(X_test)
test_loss = criterion(y_pred, y_test)
print(f"Test loss: {test_loss.item():.4f}")
