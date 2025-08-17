import streamlit as st
from formulas.math_formulas import math_formulas
from formulas.science_formulas import science_formulas
from utils.example_generator import generate_example
from pathlib import Path

# Load custom styles
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Page config
st.set_page_config(
    page_title="PROMPTO STEM Agent",
    page_icon="assets/images/favicon.png",
    layout="centered"
)

# Header with logo
st.image("assets/images/prompto-logo.png", width=140)
st.title("PROMPTO: Your STEM Formula Buddy 🧠")

# Subject and grade selection
subject = st.selectbox("Choose Subject", ["Math", "Science"])
grade = st.selectbox("Choose Grade", sorted(set(math_formulas.keys()) | set(science_formulas.keys())))

# Load formulas
formulas = math_formulas.get(grade, {}) if subject == "Math" else science_formulas.get(grade, {})
topic = st.selectbox("Choose Topic", list(formulas.keys()) if formulas else [])
formula_list = formulas.get(topic, {})

# Display formulas and examples
for name, formula in formula_list.items():
    st.subheader(f"📘 {name}")
    st.markdown(f"**Formula:** {formula}")
    if st.button(f"Explain '{name}'", key=name):
        example = generate_example(subject, grade, topic, name)
        st.markdown(f"🧠 **Example:** {example}")
