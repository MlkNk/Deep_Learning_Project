from transformers import pipeline
from transformers import BertTokenizer, BertForSequenceClassification
import torch
import os
import streamlit as st

LABELS = ['Anxiety', 'Bipolar', 'Depression', 'Normal', 'Personality disorder', 'Stress', 'Suicidal']

# Chargement unique
@st.cache_resource

def load_model():
    model_path = "bert_model_final"
    tokenizer = BertTokenizer.from_pretrained(model_path)
    model = BertForSequenceClassification.from_pretrained(model_path)
    model.eval()
    return tokenizer, model



tokenizer, model = load_model()

@st.cache_resource
def load_translator():
    return pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")

def translate_text(text, source_lang):
    if source_lang == "Français":
        translator = load_translator()
        return translator(text, max_length=512)[0]['translation_text']
    return text

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1).squeeze()
    pred_idx = torch.argmax(probs).item()
    return LABELS[pred_idx], probs
