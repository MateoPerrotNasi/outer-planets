import streamlit as st

from pages.data import data
from pages.goldilock_zone import goldilock_zone
from pages.systems import systems

st.set_page_config(page_title="Outer Planets", page_icon="🪐", layout="wide")

st.sidebar.image("OP-logo-2.png", use_column_width=True)


# Load app page content
def app():
    st.title("Welcome to the Outer Planets Project")
    st.image("OP-logo-2.png", use_column_width=True)
    st.write("""
    Outer Planets est un projet de recherche qui a pour but de prédire si une exoplanète est située dans 
    une zone potentiellement habitable. Pour cela, nous allons utiliser un modèle de machine learning qui prend en 
    entrée les caractéristiques de l’exoplanète et qui prédit si elle est située dans une zone habitable ou non. """)
    st.write("""Outer Planets est un data storytelling qui raconte l'histoire d'exoplanètes découvertes par plusieurs 
    laboratoires de recherche. Ces exoplanètes sont des planètes situées en dehors de notre système solaire. Un des 
    buts de ce projet est de prédire si une exoplanète est située dans une zone habitable de son système ou non. Pour 
    cela, nous allons utiliser un modèle de machine learning qui prend en entrée les caractéristiques de l'exoplanète 
    et qui prédit si elle est située dans une Goldilocks zone ou non. """)


# Display the app page
app()
