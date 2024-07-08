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

    # Navigation
    st.header("Navigation")
    st.write("Utilisez les boutons ci-dessous pour explorer les différentes sections de ce projet.")

    if st.button("📊 Exploration des Données"):
        st.write(
            "Plongez dans les données brutes et découvrez les caractéristiques des exoplanètes et de leurs étoiles hôtes.")

    if st.button("📈 Visualisation des Données"):
        st.write(
            "Visualisez les relations entre différentes caractéristiques des exoplanètes à l'aide de graphiques interactifs.")

    if st.button("🤖 Modèles de ML"):
        st.write(
            "Apprenez comment les algorithmes de machine learning peuvent être utilisés pour prédire les propriétés des exoplanètes.")

    if st.button("🔍 Importance des Caractéristiques"):
        st.write("Découvrez quelles caractéristiques sont les plus importantes pour les modèles de prédiction.")

    if st.button("🔮 Prédictions Interactives"):
        st.write("Entrez vos propres données pour prédire les caractéristiques d'une exoplanète.")

    if st.button("📈 Tendances et Insights"):
        st.write("Analysez les tendances et obtenez des insights approfondis sur les données.")

    if st.button("ℹ️ À propos"):
        st.write("Informations sur le projet, les sources de données et les références.")

    st.write("---")
    st.write("Projet réalisé par PERROT--NASI Matéo et TOMATIS Margot. Pour plus d'informations, vous pouvez nous "
             "retrouver sur nos github.")


# Display the app page
app()
