import torch
from torchvision import transforms

# Define the transforms to be applied to the input data
data_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
])

def preprocess_data(data_dir, annotations_file, batch_size=32, shuffle=True, num_workers=4):
    """
    Preprocess the data and create a PyTorch DataLoader for training and validation.
    """
    dataset = CustomImageDataset(annotations_file, data_dir, transform=data_transforms)
    dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers)
    return dataloader