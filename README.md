# 📊 Analyse des données éducatives — Sélection de pays pour une academy

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?logo=pandas)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)


## 🎯 Objectif du projet

Ce projet vise à identifier les **pays les plus pertinents pour l’implantation d’une academy (centre de formation)** à partir de données éducatives issues de la base **EdStats (Banque mondiale)**.

L’objectif est de construire une **méthode d’aide à la décision basée sur les données** afin de guider une stratégie d’expansion internationale.


## 📁 Données utilisées

📌 Source : **Banque mondiale **

Les indicateurs couvrent plusieurs dimensions :

- 👥 Démographie (population, croissance)
- 🎓 Éducation (taux de scolarisation, alphabétisation)
- 💰 Économie (revenu par habitant)
- 🌐 Numérique (accès à Internet)

---

## 🧠 Méthodologie

### 🔹 1. Préparation des données
- Nettoyage des données
- Gestion des valeurs manquantes
- Sélection des indicateurs pertinents

### 🔹 2. Construction du dataset
- Transformation en tableau **pays × indicateurs**
- Calcul d’une moyenne sur plusieurs années

### 🔹 3. Analyse des corrélations
- Corrélations de Pearson & Spearman
- Suppression des indicateurs redondants (|corr| > 0.7)

### 🔹 4. Analyse univariée
- Statistiques descriptives (`describe()`)
- Visualisation (`displot`)
- Interprétation des distributions

### 🔹 5. Scoring des pays
- Normalisation (MinMaxScaler)
- Pondération des indicateurs
- Calcul d’un score global

### 🔹 6. Sélection des pays
- Classement des pays
- Identification des marchés prioritaires


## ⚙️ Installation de l'environnement

Ce projet utilise **uv** pour gérer les dépendances et garantir la reproductibilité de l’environnement.

### 🔧 Prérequis

- Python ≥ 3.14
- uv installé

👉 Installation de uv :

```bash
git clone https://github.com/djibrilba38/OPC_Project_02.git
cd OPC_Project_02
python3 -m venv .venv
source .venv/bin/activate
pip install uv
uv sync

##Pour télécharger les données :
uv run python scripts/download_data.py


# 🚀  Ready to start 
