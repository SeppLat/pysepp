import torch
import torch.nn.functional as functional
import torch.nn as nn

#Testscript, if pytorch is installed
class MainNet(nn.Module):
    def __init__(self):
        super(MainNet, self).__init__()
        self.linear1 = nn.Linear(10, 10)

    def forward(self, x):
        x = functional.relu(self.linear1(x))

    def num_flat_features(self, x):
        pass

net1 = MainNet()
print(MainNet)