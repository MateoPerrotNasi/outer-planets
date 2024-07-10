import streamlit as st


st.set_page_config(page_title="Outer Planets", page_icon="🪐", layout="wide")

st.sidebar.image("./OP-logo-2.png", use_column_width=True)


# Load app page content
def app():
    st.title("Bienvenue sur le projet Outer Planets")
    st.image("OP-logo-2.png", use_column_width=True)
    st.write("""
    Bienvenue dans notre exploration des exoplanètes ! Ce projet vise à découvrir et à analyser les données fascinantes des planètes situées en dehors de notre système solaire.
    Les exoplanètes sont des corps célestes qui orbitent autour d'étoiles autres que notre Soleil. Grâce aux progrès technologiques et aux missions spatiales, des milliers d'exoplanètes ont été découvertes, chacune avec ses caractéristiques uniques.
    """)

    st.write("---")
    st.write("Projet réalisé par PERROT--NASI Matéo et TOMATIS Margot. Pour plus d'informations, vous pouvez nous "
             "retrouver sur nos github.")


# Display the app page
app()
