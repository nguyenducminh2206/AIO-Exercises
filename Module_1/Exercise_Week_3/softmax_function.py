import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.exp(x) / torch.sum(torch.exp(x), dim=0)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdims=True)
        exps = torch.exp(x - x_max.values)
        sum_exps = exps.sum(0, keepdims=True)
        return exps / sum_exps


# Example data
data = torch.Tensor([1, 2, 3])

# Softmax example
softmax = Softmax()
output = softmax(data)
print("Softmax Output:", output)

# Softmax Stable example
softmax_stable = SoftmaxStable()
output_stable = softmax_stable(data)
print("Stable Softmax Output:", output_stable)
