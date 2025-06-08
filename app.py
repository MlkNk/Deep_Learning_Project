import streamlit as st
import matplotlib.pyplot as plt
import torch

st.set_page_config(page_title="🧠 Mental Health Classifier", layout="wide")

from utils import translate_text, predict, LABELS
from download_model import download_model

@st.cache_resource
def load_model():
    model_path = os.path.join(".", "bert_model_final")
    #commenter la ligne ci dessus pour modèle en ligne
    tokenizer = BertTokenizer.from_pretrained(model_path)
    model = BertForSequenceClassification.from_pretrained(model_path)
    model.eval()
    return tokenizer, model

download_model()

# --- UI setup ---

st.title("🧠 Mental Health Text Classifier")
st.markdown("Détection automatique de troubles psychologiques à partir d’un texte libre. Basé sur **BERT fine-tuné**.")

col1, col2 = st.columns([3, 1])

with col1:
    text = st.text_area("✍️ Entrez un texte (Français ou Anglais)", height=200)

with col2:
    language = st.selectbox("Langue du texte :", ["Français", "English"])
    show_probs = st.checkbox("Afficher les probabilités")

if st.button("🔍 Analyser"):
    if text.strip():
        translated = translate_text(text, language)
        prediction, probabilities = predict(translated)
        st.success(f"### ✅ Prédiction : **{prediction}**")

        if show_probs:
            st.subheader("📊 Distribution des probabilités")
            fig, ax = plt.subplots()
            ax.barh(LABELS, probabilities.numpy(), color="skyblue")
            ax.set_xlim(0, 1)
            st.pyplot(fig)
    else:
        st.warning("Veuillez entrer un texte à analyser.")

st.sidebar.markdown("### 📁 Infos modèle")
st.sidebar.markdown("""
- Modèle : BERT-base (HuggingFace)
- Fine-tuning : 3 epochs sur données Reddit
- F1-macro : **0.78**
- 7 classes : Anxiety, Bipolar, Depression, Normal, Personality disorder, Stress, Suicidal
""")
