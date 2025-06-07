# backend/app.py
from flask import Flask, request, jsonify
from flask_compress import Compress
from PIL import Image
import torch
from torchvision import transforms
from model import DRNet

# Config
input_size = 224
mean, std = [0.485,0.456,0.406], [0.229,0.224,0.225]
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load
model = DRNet(input_size,2)
model.load_state_dict(torch.load('dr_model.pth', map_location=device))
model.to(device).eval()

# Transform
transform = transforms.Compose([
    transforms.Resize(input_size),
    transforms.ToTensor(),
    transforms.Normalize(mean,std)
])

app = Flask(__name__)
Compress(app)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify(error='Pas de fichier'), 400
    img = Image.open(request.files['image'].stream).convert('RGB')
    x = transform(img).unsqueeze(0).to(device)
    with torch.no_grad():
        pred = model(x).argmax(1).item()
    texts = {0:'No Retinopathy',1:'Diabetic Retinopathy'}
    return jsonify(code=pred, label=texts[pred])

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
