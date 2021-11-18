import streamlit as st

from gordon.utils import load_image, spacing, line, render_lines, render_paragraph

st.set_page_config(
    layout="wide", page_title="Domonique Gordon", page_icon="📈"
)


st.title("Domonique Gordon")
st.markdown("Data Engineer | Python Programmer | Navy Veteran")
spacing()
profile_col, mission_col = st.columns([1, 2])




with profile_col:
    path = "profile_pic.png"
    image = load_image(path, 500)
    st.image(image)

with mission_col:
    section = "Mission Statement"
    st.subheader(section)
    path = f"about_me/{section}"
    render_paragraph(path)

    section = "About Me"
    st.subheader(section)
    path = f"about_me/{section}"
    render_paragraph(path)




line()

tech, soft, cloud = st.columns(3)
with tech:
    section = "Technical Skills"
    st.subheader(section)
    render_lines(section)

with soft:
    section = "Soft Skills"
    st.subheader(section)
    render_lines(section)

with cloud:
    section = "Cloud Skills"
    st.subheader(section)
    render_lines(section)

spacing()
line()

section = "Experience"
st.subheader(section)
st.caption("Curology 2020 - Present")
render_lines(section)

spacing()
line()

education, contact = st.columns(2)
with education:
    section = "Education"
    st.subheader(section)
    render_lines(section.lower(), sort=False)

with contact:
    section = "Contact"
    st.subheader(section)
    render_lines(section, sort=False)

spacing()
line()

st.subheader("Performance Reviews")
with st.expander("Click to expand"):
    st.caption("Source - Manager (Data Engineering) - 08/09/2021")
    render_paragraph("reviews/engineering_manager")

    spacing()

    st.caption("Source - Senior Data Engineer College - 07/26/2021")
    render_paragraph("reviews/senior_engineer")

