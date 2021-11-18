import streamlit as st
from PIL import Image

@st.cache
def load_image(path, size=300):
    path = f"gordon/images/{path}"
    image = Image.open(path)
    if size:
        image = image.resize((size, size))
    return image


def spacing(lines=3):
    for _ in range(lines):
        st.write("")


def line():
    st.markdown("***")


def render_lines(name, sort=True):
    name = name.replace(" ", "_").lower()
    with open(f"gordon/text/lines/{name}.txt") as f:
        lines = f.readlines()
    if sort:
        lines = sorted(lines)
    for line in lines:
        st.markdown(f"- {line}")


def render_paragraph(name):
    name = name.replace(" ", "_").lower()
    with open(f"gordon/text/{name}.txt") as f:
        review = f.read()
    st.text(review)