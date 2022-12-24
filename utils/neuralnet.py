import torch.nn as nn
import torch.nn.functional as F

class NeuralNet(nn.Module):
  def __init__(self):
    super(NeuralNet, self).__init__()
    # Define the layers of the neural network
    self.fc1 = nn.Linear(3*4*4, 32)
    self.fc2 = nn.Linear(32, 3*4*4)

  def forward(self, x):
    # Convert the input tensor and weight tensor to the same dtype
    x = x.to(self.fc1.weight.dtype)
    weight = self.fc1.weight.to(x.dtype)

    # Reshape the input tensor to a 1D tensor
    x = x.view(1, 4*4*3)

    # Compute the model's output using the F.linear function
    x = F.linear(x, weight, self.fc1.bias)
    x = F.relu(x)
    x = F.linear(x, self.fc2.weight, self.fc2.bias)
    return x