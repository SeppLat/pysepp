import torch
import torch.nn as nn

#Testscript, if pytorch is installed
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.linear1 = nn.Linear()

    def forward(self, x):
        pass

    def num_flat_features(self, x):
        pass

net1 = Net()
print(Net)