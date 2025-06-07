# backend/train.py
import os, torch, torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from model import DRNet

# --- Hyperparams ---
input_size, batch_size, epochs, lr = 224, 16, 10, 1e-4
train_dir, val_dir = 'data/train', 'data/val'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# --- Transforms ---
mean, std = [0.485,0.456,0.406], [0.229,0.224,0.225]
transform = transforms.Compose([
    transforms.Resize(input_size),
    transforms.ToTensor(),
    transforms.Normalize(mean, std)
])

# --- DataLoaders ---
train_ds = datasets.ImageFolder(train_dir, transform=transform)
val_ds   = datasets.ImageFolder(val_dir, transform=transform)
train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True)
val_loader   = DataLoader(val_ds,   batch_size=batch_size)

# --- Model, loss, optim ---
model = DRNet(input_size, num_classes=2).to(device)
criterion = torch.nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=lr)

# --- Train loop ---
for epoch in range(1, epochs+1):
    model.train()
    running_loss = 0
    for imgs, labels in train_loader:
        imgs, labels = imgs.to(device), labels.to(device)
        preds = model(imgs)
        loss = criterion(preds, labels)
        optimizer.zero_grad(); loss.backward(); optimizer.step()
        running_loss += loss.item()
    # validation
    model.eval()
    correct, total = 0,0
    with torch.no_grad():
        for imgs, labels in val_loader:
            imgs, labels = imgs.to(device), labels.to(device)
            preds = model(imgs).argmax(1)
            correct += (preds==labels).sum().item()
            total   += labels.size(0)
    acc = correct/total*100
    print(f"Epoch {epoch}/{epochs} — loss: {running_loss/len(train_loader):.4f} — val acc: {acc:.2f}%")

# save
torch.save(model.state_dict(), 'dr_model.pth')
print("Modèle sauvegardé.")
# optionally script
traced = torch.jit.trace(model.cpu(), torch.randn(1,3,input_size,input_size))
traced.save('dr_model.pt')
