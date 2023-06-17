import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    translator = pipeline("translation_en_to_fr", "tonystark0/my_en_to_fr_translation_model")
    return translator


def translate(text, translator):
    input = f"translate English to French: {text}"
    output = translator(input)
    return output[0]["translation_text"]


translator = load_model()

st.title("Language Translation")
st.divider()
st.subheader("Input English Text")
english_txt = st.text_area("English Text", key="english", label_visibility="hidden")
clicked = st.button("Translate to French", type="primary")
st.divider()

if clicked:
    french_text = translate(english_txt, translator)
else:
    french_text = ""

st.subheader("French Translation")
st.text_area("French Text", french_text, key="french", label_visibility="hidden")