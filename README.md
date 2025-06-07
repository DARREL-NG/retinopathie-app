# Vue 3 + Vite

This template should help get you started developing with Vue 3 in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

Learn more about IDE Support for Vue in the [Vue Docs Scaling up Guide](https://vuejs.org/guide/scaling-up/tooling.html#ide-support).
# 🧠 Diagnostic de la Rétinopathie Diabétique

![CI](https://img.shields.io/badge/build-passing-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue) ![Version](https://img.shields.io/badge/version-1.0.0-orange)

Plateforme web de diagnostic automatique de la rétinopathie diabétique à partir d’images du fond d’œil.  
**Stack** : React (frontend) • Node.js/Express (API) • Flask/Python (IA) • PyTorch (entraînement)

---

## 📋 Table des matières

1. [Contexte & fonctionnalités](#contexte--fonctionnalités)  
2. [Architecture](#architecture)  
3. [Prérequis](#prérequis)  
4. [Installation](#installation)  
5. [Organisation des données](#organisation-des-données)  
6. [Entraînement du modèle](#entraînement-du-modèle)  
7. [Configuration](#configuration)  
8. [Démarrage de l’application](#démarrage-de-lapplication)  
9. [Utilisation](#utilisation)  
10. [API Reference](#api-reference)  
11. [Structure du projet](#structure-du-projet)  
12. [Exemples de commande](#exemples-de-commande)  
13. [Tests](#tests)  
14. [Déploiement](#déploiement)  
15. [Contribuer](#contribuer)  
16. [Licence](#licence)  
17. [Remerciements & références](#remerciements--références)  
18. [Auteur & Contact](#auteur--contact)  

---

## Contexte & fonctionnalités

**Problématique** : Les patients diabétiques nécessitent un dépistage régulier de la rétinopathie. L’IA permet d’automatiser l’analyse des images du fond d’œil, d’alléger la charge des ophtalmologistes et d’améliorer l’accès au dépistage.

**Fonctionnalités clés** :
- Upload d’une image de rétine (JPEG/PNG)  
- Diagnostic IA binaire (rétinopathie : oui/non + score de confiance)  
- Interface utilisateur responsive (desktop & mobile)  
- Historique des diagnostics (en option)  
- Modularité : micro-services isolés (React ↔ Express ↔ Flask)

---

## Architecture

```text
[Frontend React]  ↔  [API Express]  ↔  [Micro-service Flask/IA]
                                        └── Modèle PyTorch (dr_model.pt)
Prérequis
Node.js ≥ 14

npm ou yarn

Python ≥ 3.8

pip

(Optionnel) GPU CUDA pour entraînement

Git, Docker (si containerisé)
Cloner le dépôt

bash

git clone https://github.com/darrelng2.0@gmail.com/retinopathie-app.git
cd retinopathie-app
Installer les dépendances

Frontend :

bash

cd client
npm install
Backend Express :

bash

cd ../server
npm install
API Flask & IA :

bash

cd ../ai_model
pip install -r requirements.txt
Entraînement PyTorch :

bash

cd ../backend
pip install -r requirements.txt

Organisation des données
Place tes images classées dans la structure :

bash

data/
├── train/
│   ├── 0/      # Sans rétinopathie
│   └── 1/      # Avec rétinopathie
└── val/
    ├── 0/
    └── 1/
Les dossiers 0 et 1 contiennent chacun des images JPEG/PNG.

Entraînement du modèle
Lancer l’entraînement

bash

cd backend
python train.py
Génère dr_model.pth (poids)

Génère dr_model.pt (TorchScript)

Résultats

Courbe de loss & accuracy en console

Modèles sauvegardés dans backend/

Configuration
Crée un fichier .env à la racine (s’appuie sur .env.example) :

dotenv

# server/.env
PORT=3001

# ai_model/.env
FLASK_PORT=5000
MODEL_PATH=../backend/dr_model.pt
Démarrage de l’application
API IA (Flask)

bash

cd ai_model
python app.py
API Express

bash

cd ../server
npm start
Frontend React

bash

cd ../client
npm start
Ouvre http://localhost:3000 dans ton navigateur.

Utilisation
Clique sur "Choisir un fichier" et sélectionne une image de rétine.

Clique sur "Diagnostiquer".

Lis le résultat :

diagnostic: "rétinopathie détectée"

score: 0.87

API Reference
POST /api/diagnose
Description : Envoie une image au backend pour diagnostic

Headers :
Content-Type: multipart/form-data

Form Data :

image : fichier image (JPEG/PNG)

Réponse (200 HTTP) :

json

{
  "diagnostic": "rétinopathie détectée",
  "score": 0.87
}
POST http://localhost:5000/predict
Payload (JSON) :

json
r
{ "image_path": "uploads/abcdef.jpg" }
Réponse (JSON) :

json

{ "diagnostic": "rétinopathie détectée", "score": 0.87 }
Structure du projet

retinopathie-app/
├── client/          # React
│   └── src/
├── server/          # Node.js + Express
│   └── index.js
├── ai_model/        # Flask + IA
│   └── app.py
├── backend/         # Entraînement PyTorch
│   ├── train.py
│   └── model.py
├── data/            # Datasets (train/val)
└── README.md        # ← Ce fichier



Flask affiche la prédiction

Express log l’upload et la réponse

Tests
(À implémenter si nécessaire)

Frontend : Jest + React Testing Library

Backend : Jest ou Mocha

IA : pytest pour vérifier la chargement du modèle



