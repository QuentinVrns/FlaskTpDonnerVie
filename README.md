# Projet Fournisseurs (Flask + Pydantic)

Ce projet est un petit site web en **Flask** permettant de gérer des fournisseurs (ajout, modification, liste).  
Il utilise **Pydantic** pour valider les données du formulaire et une **liste en mémoire** comme stockage (pas de base de données).

---

## 🚀 Fonctionnalités

- ✅ Liste des fournisseurs (tableau Bootstrap)
- ✅ Ajout d’un fournisseur via formulaire
- ✅ Modification d’un fournisseur existant
- ✅ Validation des champs avec **Pydantic** (ex. email correct, nom non vide…)
- ✅ Architecture claire et sans doublon :
  - **base.html** pour le header/footer commun
  - **CSS/JS** regroupés dans `static/`
  - **Formulaire unique** pour ajouter et modifier

---

## 📂 Structure du projet

projet_fournisseurs/
├─ app.py                # Routes Flask
├─ models.py             # Modèle Supplier (Pydantic)
├─ services.py           # Service CRUD en mémoire
├─ requirements.txt      # Dépendances Python
├─ templates/            # Templates HTML (Jinja2)
│  ├─ base.html
│  ├─ suppliers_list.html
│  └─ supplier_form.html
└─ static/               # Fichiers statiques
   ├─ css/style.css
   └─ js/app.js

---

## ⚙️ Installation

### 1. Cloner ou créer le projet
git clone git@github.com:QuentinVrns/FlaskTpDonnerVie.git

cd projet_fournisseurs

### 2. Créer et activer un environnement virtuel
python3 -m venv venv

source venv/bin/activate

### 3. Installer les dépendances
pip install -r requirements.txt

---

## ▶️ Lancer le projet

Sous Linux/macOS :

export FLASK_APP=app.py

flask run

Sous Windows (CMD) :

set FLASK_APP=app.py

flask run

Puis ouvrir :
http://127.0.0.1:5000

---

## 📌 Remarques

- Les fournisseurs sont **stockés en mémoire** → si vous redémarrez le serveur, la liste est réinitialisée.
- Pour un vrai projet, il faudrait remplacer `services.py` par une base de données (SQLite, PostgreSQL…).

---

## 👨‍💻 Auteur

Projet développé dans le cadre d’un exercice Flask + Pydantic.
