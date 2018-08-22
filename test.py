import numpy as np
import torch
from torch.autograd import Variable

tensor = torch.rand(2,2,)
x = Variable(tensor, requires_grad=True)

print tensor
print x

test_list = ['aa', 'bb']

for i in test_list:
    print(i)



