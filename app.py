
import streamlit as st
import joblib

@st.cache_resource
def load_models():
    models = {}
    models["Naive Bayes"] = joblib.load("naive_bayes_sentiment_model.pkl")
    models["Logistic Regression"] = joblib.load("logistic_regression_sentiment_model.pkl")

import pickle
import numpy as np

# Load models
@st.cache_resource
def load_models():
    models = {}
    with open("naive_bayes_sentiment_model.pkl", "rb") as f:
        models["Naive Bayes"] = pickle.load(f)
    with open("logistic_regression_sentiment_model.pkl", "rb") as f:
        models["Logistic Regression"] = pickle.load(f)

    return models

models = load_models()

st.sidebar.title("Model Info")
st.sidebar.write("""
Select a model and enter text to classify.
Models available:
- Naive Bayes
- Logistic Regression
""")

st.title("Text Classification Demo")
st.markdown("### Try out different models on your text input!")

model_choice = st.selectbox("Choose a model:", list(models.keys()))
user_input = st.text_area("Enter text to classify:", height=150)

if st.button("Predict"):
    if user_input.strip():
        model = models[model_choice]
        prediction = model.predict([user_input])[0]

        st.success(f"**Prediction:** {prediction}")


        if hasattr(model, "predict_proba"):
            probs = model.predict_proba([user_input])[0]
            st.markdown("#### Prediction Probabilities")
            for i, p in enumerate(probs):
                st.write(f"Class {i}: {p:.4f}")
    else:
        st.warning("Please enter some text.")

st.markdown("---")
st.caption("Built with Streamlit | Demo for ML Model Showcase")