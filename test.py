import torch

# print(torch.arange(1,6,dtype=torch.float))
# tensor([1., 2., 3., 4., 5.])


#unsqueeze adds a extra dimension to every element
# If a tensor has shape [5], unsqueeze(0) would change its shape to [1, 5] and unsqueeze(1) would change its shape to [5, 1].
# print(torch.arange(1,6,dtype=torch.float)).unsqueeze(1)
#  tensor([[1.],
#         [2.],
#         [3.],
#         [4.],
#         [5.]])

# print(torch.arange(1,6,dtype=torch.float)).unsqueeze(1)
#  tensor([[1.],[2.],[3.],[4.],[5.]])
print(torch.version.cuda)
device = "cuda" if torch.cuda.is_available() else "mps" if torch.has_mps or torch.backends.mps.is_available() else "cpu"
print(device)
print(torch.cuda.is_available())

