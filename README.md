
---
## Auteurs 
- MALAÏKA NKUIDA
- INES SEKARI


## Contenu du projet

```
mental_health_nlp/
├── app.py                      # Application Streamlit pour prédiction en temps réel
├── bert_model_final/          # Modèle BERT fine-tuné (via Hugging Face Transformers)
├── notebook/
│   └── Projet_DeepLearning.ipynb  # Notebook principal : EDA + Modélisation
├── requirements.txt           # Librairies nécessaires
└── README.md                  # Documentation (ce fichier)
```


## Objectif du projet : Mental Health NLP Classifier - Reddit Comments

Ce projet NLP vise à détecter différents troubles de santé mentale (anxiété, stress, dépression, etc.) à partir de commentaires Reddit, en comparant des modèles classiques de machine learning à un modèle BERT de type Transformer.

Le projet explore les performances de 3 approches différentes :
- Modèles classiques : Logistic Regression, SVM (avec TF-IDF)
- Modèle avancé : BERT pré-entraîné avec fine-tuning via Hugging Face

---

## Jeu de données

Le jeu de données est issu de [Kaggle](https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health/data) : il contient plus de 10 000 commentaires Reddit labellisés selon différents troubles psychologiques :

| Classe                 | Exemple             |
|------------------------|---------------------|
| Normal                | Aucun trouble détecté |
| Depression            | Symptômes dépressifs |
| Anxiety               | Manifestations anxieuses |
| Suicidal              | Idées suicidaires |
| Bipolar               | Symptômes bipolaires |
| Personality disorder  | Troubles de la personnalité |
| Stress                | Stress chronique ou aigu |

---

## Méthodologie

1. **Analyse exploratoire ** : exploration, nettoyage, lemmatisation
2. **Vectorisation** : TF-IDF pour les modèles classiques
3. **Modélisation** :
   - Régression logistique
   - SVM
   - BERT (`bert-base-uncased`, fine-tuning sur 3 epochs)
4. **Évaluation** :
   - Accuracy
   - F1-score macro et par classe
   - Matrice de confusion
   - Visualisation F1-score par classe

---

## Résultats comparés

| Modèle              | Accuracy | F1 Macro | F1 Stress | Temps d'entraînement |
|---------------------|----------|----------|-----------|-----------------------|
| Logistic Regression | 0.7500   | 0.6880   | 0.52      | ~20 sec               |
| SVM                 | 0.7503   | 0.7094   | 0.56      | ~120 secsec               |
| BERT (3 epochs)     | **0.7954** | **0.7809** | **0.68** | ~966 sec             |

---

## Application Streamlit

L'application permet :
- D'explorer le dataset de base
- D’entrer un texte libre et de prédire automatiquement la catégorie mentale associée

### Lancer l'application :

```bash

## Déploiement

Vous pouvez déployer l'application en ligne via :

- Streamlit Cloud (https://streamlit.io/cloud)


## Installation

### En local :

```bash
git clone https://github.com/MlkNk/Deep_Learning_Project.git
cd mental_health_nlp
pip install -r requirements.txt

streamlit run app.py
```

## **Note importante sur le déploiement en ligne :

Le modèle BERT fine-tuné (./bert_model_final/) utilisé possède un fichier lourd (précisement `model.safetensors` : taille ~417 Mo) qui ne peut pas être versionné sur GitHub ni chargé directement via Streamlit Cloud, en raison des limitations techniques (limite de 100 Mo par fichier sur GitHub, et limitations de Streamlit Cloud).

> Ce fichier contient les poids du modèle BERT fine-tuné utilisé pour la classification des textes. Il est nécessaire pour exécuter les prédictions avec l'application Streamlit (`app.py`).

### ** L'application fonctionne parfaitement en local avec : streamlit run app.py dans le terminal qui du dossier du projet.

** Il sera fourni séparément, bien vouloir l'intégrer dans le dossier.

