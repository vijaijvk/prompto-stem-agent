import streamlit as st
from formulas.math_formulas import math_formulas
from formulas.science_formulas import science_formulas
from utils.example_generator import generate_example

st.set_page_config(page_title="PROMPTO", page_icon="🧠")

st.title("🧠 PROMPTO: STEM Formula Explainer")
subject = st.selectbox("Choose Subject", ["Math", "Science"])
grade = st.selectbox("Choose Grade", sorted(set(math_formulas.keys()) | set(science_formulas.keys())))

if subject == "Math":
    formulas = math_formulas.get(grade, {})
else:
    formulas = science_formulas.get(grade, {})

topic = st.selectbox("Choose Topic", list(formulas.keys()) if formulas else [])
formula_list = formulas.get(topic, {})

for name, formula in formula_list.items():
    st.subheader(f"📘 {name}")
    st.markdown(f"**Formula:** {formula}")
    if st.button(f"Explain '{name}'", key=name):
        example = generate_example(subject, grade, topic, name)
        st.markdown(f"🧠 **Example:** {example}")
