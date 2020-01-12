import torch

a = torch.rand(2, 1, 3)
b = torch.rand(2, 1, 3)
c = torch.cat([a, b], dim=2)  # 按第0维度进行拼接，除拼接之外的维度必须相同

print(a)
print(b)
print(torch.split(c, 3, 2))
