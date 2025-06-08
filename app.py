import streamlit as st
import os
import torch
from transformers import BertTokenizer, BertForSequenceClassification
import matplotlib.pyplot as plt

# Liste des labels dans l'ordre de ton fine-tuning
LABELS = ['Anxiety', 'Bipolar', 'Depression', 'Normal', 'Personality disorder', 'Stress', 'Suicidal']

st.set_page_config(page_title="Mental Health Classifier", layout="centered")
print("Contenu du dossier bert_model_final :", os.listdir("./bert_model_final"))

@st.cache_resource
def load_model():
    model_path = os.path.join(".", "bert_model_final")
    #commenter la ligne ci dessus pour modèle en ligne
    tokenizer = BertTokenizer.from_pretrained(model_path)
    model = BertForSequenceClassification.from_pretrained(model_path)
    model.eval()
    return tokenizer, model

tokenizer, model = load_model()


def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    probs = torch.softmax(logits, dim=1).squeeze()
    predicted_class_id = torch.argmax(probs).item()
    return LABELS[predicted_class_id], probs

# --- UI Streamlit ---

#st.set_page_config(page_title="Mental Health Classifier", layout="centered")

st.title("Mental Health Text Classifier")
st.markdown("Ce modèle prédit un **trouble psychologique** à partir d’un texte libre. Il utilise un modèle **BERT fine-tuné** sur un dataset Reddit issu de Kaggle.")

st.sidebar.title("À propos")
st.sidebar.markdown("""
Projet NLP | Transfert Learning  
Modèle utilisé : `BERT-base`  
Entrainement : 3 epochs, fine-tuning complet  
F1-macro : **0.78**  
""")

user_input = st.text_area("Entrez un texte (en anglais) :", height=200)

show_probs = st.checkbox("Afficher les probabilités pour chaque classe")

if st.button("Prédire"):
    if user_input.strip():
        prediction, probabilities = predict(user_input)
        st.success(f"### Prédiction : {prediction}")
        
        if show_probs:
            st.subheader("Probabilités par classe")
            prob_dict = {LABELS[i]: float(probabilities[i]) for i in range(len(LABELS))}
            st.bar_chart(prob_dict)
    else:
        st.warning("Veuillez entrer un texte à analyser.")

