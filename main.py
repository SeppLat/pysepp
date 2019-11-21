import torch
import torch.nn as nn

#Testscript, if pytorch is installed
class FirstNet(nn.Module):
    def __init__(self):
        super(FirstNet, self).__init__()
        self.linear1 = nn.Linear(10, 10)
        self.linear2 = nn.Linear(10, 10)

    def forward(self, x):
        pass

    def num_flat_features(self, x):
        pass

net1 = FirstNet()
print(FirstNet)