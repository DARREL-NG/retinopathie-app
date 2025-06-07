# backend/model.py
import torch.nn as nn

class DRNet(nn.Module):
    def __init__(self, input_size=224, num_classes=2):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(64,128,3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(128,256,3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
        )
        feat_map = input_size // 16
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(256*feat_map*feat_map, 512), nn.ReLU(), nn.Dropout(0.5),
            nn.Linear(512, num_classes)
        )
    def forward(self, x):
        x = self.features(x)
        return self.classifier(x)
