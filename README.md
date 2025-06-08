
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
│   └── analyse_DeepLearningL.ipynb  # Notebook principal : EDA + Modélisation
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

Le jeu de données est issu de [Kaggle](https://www.kaggle.com/) : il contient plus de 10 000 commentaires Reddit labellisés selon différents troubles psychologiques :

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
streamlit run app.py


## Déploiement (optionnel)

Vous pouvez déployer l'application en ligne via :
- [Streamlit Cloud](https://streamlit.io/cloud)
- Hugging Face Spaces (si modèle public)

## 📦 Installation

### En local :

```bash
git clone https://github.com/<nom-utilisateur>/mental_health_nlp.git
cd mental_health_nlp
pip install -r requirements.txt
```

