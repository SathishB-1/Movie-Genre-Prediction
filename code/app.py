import streamlit as st
import joblib
import re

# Load model and vectorizer
model = joblib.load("movie_genre_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# App title
st.set_page_config(page_title="Movie Genre Predictor")
st.title("🎬 Movie Genre Prediction App")
st.write("Upload a `.txt` file containing movie descriptions to predict their genres.")

# File uploader
uploaded_file = st.file_uploader("📂 Upload Description File (.txt)", type=["txt"])

if uploaded_file is not None:
    # Read and decode content
    content = uploaded_file.read().decode("utf-8")

    # Split into individual descriptions using regex
    entries = re.findall(r'\d+\s*:::\s*.*?:::\s*(.*?)(?=\d+\s*:::|$)', content, re.DOTALL)

    if not entries:
        st.warning("No valid movie descriptions found.")
    else:
        st.subheader("📖 Movie Descriptions & Predicted Genres:")
        for i, desc in enumerate(entries, 1):
            cleaned_desc = desc.strip()
            if cleaned_desc:
                input_vec = vectorizer.transform([cleaned_desc])
                prediction = model.predict(input_vec)[0]
                st.markdown(f"**{i}. Genre:** 🎯 _{prediction}_\n\n> {cleaned_desc}")
