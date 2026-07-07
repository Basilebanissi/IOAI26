# Guide de Configuration ML/DL

> Un environnement de travail pour le Deep Learning en Python, configuré pas à pas.

---

## Table des matières

1. [Prérequis système](#1-prérequis-système)
2. [Installation de Python](#2-installation-de-python)
3. [Installation de VS Code](#3-installation-de-vs-code)
4. [Installation de Git](#4-installation-de-git)
5. [Cloner un dépôt GitHub](#5-cloner-un-dépôt-github)
6. [Créer un environnement virtuel Python](#6-créer-un-environnement-virtuel-python)
7. [Installation des bibliothèques essentielles](#7-installation-des-bibliothèques-essentielles)
8. [Vérification de l&#39;installation](#8-vérification-de-linstallation)
9. [Structure de projet recommandée](#9-structure-de-projet-recommandée)
10. [Ressources pour aller plus loin](#10-ressources-pour-aller-plus-loin)

---

## 1. Prérequis système

| Composant       | Minimum recommandé                              |
| --------------- | ------------------------------------------------ |
| OS              | Windows 10/11, macOS 12+, Ubuntu 20.04+          |
| RAM             | 8 Go (16 Go recommandé)                         |
| Stockage        | 20 Go libres                                     |
| GPU (optionnel) | NVIDIA avec CUDA 11.8+ pour l'accélération GPU |
| Connexion       | Requise pour l'installation des dépendances     |

---

## 2. Installation de Python

**Lien officiel :** https://www.python.org/downloads/

La version recommandée est **Python 3.10** ou **3.11** (TensorFlow et PyTorch supportent ces versions de façon stable).

### Windows

1. Télécharger l'installateur sur https://www.python.org/downloads/windows/
2. Lancer le `.exe` téléchargé
3. **Cocher impérativement** la case `Add Python to PATH` avant de cliquer sur *Install Now*
4. Vérifier l'installation en ouvrant un terminal (PowerShell ou Invite de commandes) :

```bash
python --version
pip --version
```

### macOS

```bash
# Avec Homebrew (recommandé)
# Installer Homebrew si absent : https://brew.sh
brew install python@3.11

python3 --version
pip3 --version
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip -y

python3 --version
pip3 --version
```

---

## 3. Installation de VS Code

**Lien officiel :** https://code.visualstudio.com/

### Étapes d'installation

1. Télécharger l'installateur correspondant à votre système d'exploitation
2. Suivre l'assistant d'installation (options par défaut suffisent)
3. Lancer VS Code

### Extensions indispensables

Ouvrir VS Code, puis installer les extensions suivantes via le panneau Extensions (`Ctrl+Shift+X`) :

| Extension       | Identifiant                   | Utilité                      |
| --------------- | ----------------------------- | ----------------------------- |
| Python          | `ms-python.python`          | Support Python complet        |
| Pylance         | `ms-python.vscode-pylance`  | Autocomplétion avancée      |
| Jupyter         | `ms-toolsai.jupyter`        | Notebooks Jupyter intégrés  |
| GitLens         | `eamodio.gitlens`           | Visualisation Git avancée    |
| Black Formatter | `ms-python.black-formatter` | Formatage automatique du code |

Installation via terminal VS Code (`Ctrl+` `` ` ``) :

```bash
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-toolsai.jupyter
code --install-extension eamodio.gitlens
code --install-extension ms-python.black-formatter
```

---

## 4. Installation de Git

**Lien officiel :** https://git-scm.com/downloads

### Windows

1. Télécharger l'installateur sur https://git-scm.com/download/win
2. Suivre l'assistant (conserver les options par défaut)
3. Lors du choix de l'éditeur par défaut, sélectionner **Visual Studio Code**

### macOS

```bash
# Git est souvent préinstallé. Vérifier :
git --version

# Sinon, installer via Homebrew :
brew install git
```

### Linux

```bash
sudo apt update
sudo apt install git -y
```

### Configuration initiale de Git

Exécuter ces commandes une seule fois après l'installation :

```bash
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@exemple.com"
git config --global core.editor "code --wait"
git config --global init.defaultBranch main

# Vérifier la configuration
git config --list
```

---

## 5. Cloner un dépôt GitHub

### Méthode 1 Via HTTPS (recommandée pour les débutants)

```bash
# Syntaxe générale
git clone https://github.com/utilisateur/nom-du-depot.git

# Exemple
git clone https://github.com/tensorflow/tensorflow.git

# Cloner dans un dossier spécifique
git clone https://github.com/utilisateur/nom-du-depot.git mon-dossier
```

### Méthode 2 Via SSH (recommandée pour un usage régulier)

Générer une clé SSH puis l'ajouter à votre compte GitHub :

```bash
# Générer la clé
ssh-keygen -t ed25519 -C "votre.email@exemple.com"

# Afficher la clé publique (à copier dans GitHub > Settings > SSH Keys)
cat ~/.ssh/id_ed25519.pub

# Tester la connexion
ssh -T git@github.com

# Cloner via SSH
git clone git@github.com:utilisateur/nom-du-depot.git
```

### Commandes Git essentielles après le clonage

```bash
cd nom-du-depot          # Se déplacer dans le dossier
git status               # État des fichiers modifiés
git pull                 # Récupérer les dernières modifications
git add .                # Ajouter tous les fichiers modifiés
git commit -m "message"  # Créer un commit
git push                 # Envoyer les modifications
git log --oneline        # Historique des commits
```

---

## 6. Créer un environnement virtuel Python

Il est fortement recommandé d'utiliser un environnement virtuel pour isoler les dépendances de chaque projet.

```bash
# Se placer dans le dossier du projet
cd mon-projet-dl

# Créer l'environnement virtuel
python -m venv .venv

# Activer l'environnement
# Windows (PowerShell) :
.venv\Scripts\Activate.ps1

# Windows (Invite de commandes) :
.venv\Scripts\activate.bat

# macOS / Linux :
source .venv/bin/activate

# Le prompt doit maintenant afficher (.venv)
# Pour désactiver l'environnement :
deactivate
```

### Sélectionner l'interpréteur dans VS Code

1. Ouvrir la palette de commandes : `Ctrl+Shift+P`
2. Taper : `Python: Select Interpreter`
3. Sélectionner l'interpréteur `.venv` de votre projet

---

## 7. Installation des bibliothèques essentielles

### Méthode recommandée Via requirements.txt

```bash
# S'assurer que l'environnement virtuel est activé
pip install --upgrade pip
pip install -r requirements.txt
```

### Installation manuelle Bibliothèque par bibliothèque

#### TensorFlow

**Documentation officielle :** https://www.tensorflow.org/install

```bash
# Version CPU (compatible sur toutes les machines)
pip install tensorflow

# Vérifier l'installation
python -c "import tensorflow as tf; print(tf.__version__)"
```

> **Note GPU :** Pour utiliser le GPU avec TensorFlow, installez CUDA 11.8 et cuDNN 8.6 depuis https://developer.nvidia.com/cuda-downloads, puis utilisez `pip install tensorflow[and-cuda]`.

#### PyTorch

**Documentation officielle :** https://pytorch.org/get-started/locally/

Le site officiel génère la commande d'installation adaptée à votre configuration. Exemples :

```bash
# CPU uniquement
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# CUDA 11.8 (GPU NVIDIA)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Vérifier l'installation
python -c "import torch; print(torch.__version__); print('GPU disponible :', torch.cuda.is_available())"
```

#### Streamlit

**Documentation officielle :** https://docs.streamlit.io/

```bash
pip install streamlit

# Tester avec l'application de démonstration
streamlit hello
```

#### Autres bibliothèques essentielles

```bash
# Manipulation de données
pip install numpy pandas

# Visualisation
pip install matplotlib seaborn plotly

# Machine Learning classique
pip install scikit-learn

# Notebooks Jupyter
pip install jupyterlab notebook

# Utilitaires
pip install tqdm requests python-dotenv
```

---

## 8. Vérification de l'installation

Créer un fichier `verify_setup.py` et l'exécuter pour valider l'environnement :

```python
import sys

print("=" * 50)
print("VERIFICATION DE L'ENVIRONNEMENT DEEP LEARNING")
print("=" * 50)

# Python
print(f"\nPython : {sys.version}")

# NumPy
try:
    import numpy as np
    print(f"NumPy  : {np.__version__}")
except ImportError:
    print("NumPy  : NON INSTALLE")

# Pandas
try:
    import pandas as pd
    print(f"Pandas : {pd.__version__}")
except ImportError:
    print("Pandas : NON INSTALLE")

# TensorFlow
try:
    import tensorflow as tf
    print(f"TensorFlow : {tf.__version__}")
    print(f"  GPU disponible : {len(tf.config.list_physical_devices('GPU')) > 0}")
except ImportError:
    print("TensorFlow : NON INSTALLE")

# PyTorch
try:
    import torch
    print(f"PyTorch : {torch.__version__}")
    print(f"  GPU disponible : {torch.cuda.is_available()}")
except ImportError:
    print("PyTorch : NON INSTALLE")

# Scikit-learn
try:
    import sklearn
    print(f"Scikit-learn : {sklearn.__version__}")
except ImportError:
    print("Scikit-learn : NON INSTALLE")

# Streamlit
try:
    import streamlit
    print(f"Streamlit : {streamlit.__version__}")
except ImportError:
    print("Streamlit : NON INSTALLE")

# Matplotlib
try:
    import matplotlib
    print(f"Matplotlib : {matplotlib.__version__}")
except ImportError:
    print("Matplotlib : NON INSTALLE")

print("\n" + "=" * 50)
print("Verification terminee.")
print("=" * 50)
```

```bash
python verify_setup.py
```

---

## 9. Structure de projet recommandée

```
mon-projet-dl/
├── .venv/                  # Environnement virtuel (ne pas versionner)
├── data/
│   ├── raw/                # Données brutes
│   └── processed/          # Données prétraitées
├── notebooks/              # Fichiers Jupyter (.ipynb)
├── src/
│   ├── __init__.py
│   ├── data/               # Scripts de chargement et prétraitement
│   ├── models/             # Définitions des modèles
│   └── utils/              # Fonctions utilitaires
├── outputs/
│   ├── models/             # Modèles entraînés
│   └── figures/            # Graphiques et visualisations
├── app.py                  # Application Streamlit
├── requirements.txt        # Dépendances du projet
├── .gitignore              # Fichiers à exclure de Git
└── README.md               # Documentation du projet
```

### Fichier `.gitignore` recommandé

```gitignore
# Environnement virtuel
.venv/
venv/
env/

# Fichiers Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/

# Jupyter
.ipynb_checkpoints/

# Données lourdes (à adapter selon le projet)
data/raw/
*.csv
*.h5
*.pkl

# Modèles entraînés
outputs/models/

# Variables d'environnement
.env

# IDE
.vscode/settings.json
.idea/

# macOS
.DS_Store
```

---

## 10. Ressources pour aller plus loin

### Documentation officielle

| Outil / Bibliothèque | Lien                                            |
| --------------------- | ----------------------------------------------- |
| Python                | https://docs.python.org/fr/3/                   |
| VS Code               | https://code.visualstudio.com/docs              |
| Git                   | https://git-scm.com/doc                         |
| GitHub                | https://docs.github.com/fr                      |
| TensorFlow            | https://www.tensorflow.org/learn                |
| PyTorch               | https://pytorch.org/tutorials/                  |
| Streamlit             | https://docs.streamlit.io/                      |
| NumPy                 | https://numpy.org/doc/                          |
| Pandas                | https://pandas.pydata.org/docs/                 |
| Scikit-learn          | https://scikit-learn.org/stable/user_guide.html |
| Matplotlib            | https://matplotlib.org/stable/users/index.html  |
| JupyterLab            | https://jupyterlab.readthedocs.io/              |

### Cours et tutoriels recommandés

- **Fast.ai** Cours pratique Deep Learning : https://course.fast.ai/
- **DeepLearning.AI** Spécialisations Coursera : https://www.deeplearning.ai/
- **CS231n Stanford** Réseaux de neurones convolutifs : https://cs231n.github.io/
- **Hugging Face** NLP et modèles transformers : https://huggingface.co/learn

---

*Guide rédigé pour un environnement Python 3.10/3.11. Les versions des bibliothèques peuvent évoluer se référer aux liens officiels pour les versions les plus récentes.*