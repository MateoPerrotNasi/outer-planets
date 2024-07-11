import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Chargement des données
data_path = './data/all_exoplanets_with_goldilock_zone.csv'
data = pd.read_csv(data_path)

# Configuration de la page Streamlit
st.set_page_config(page_title="Outer Planets", page_icon="🪐", layout="wide")

# Sidebar avec logo
st.sidebar.image("./OP-logo-2.png", use_column_width=True)

host_names = ['Tous les systèmes'] + list(data['Planet Host'].unique())

# Titre de la section
st.title("🌟 Influence des Etoiles Hôtes")

st.write("""
Les étoiles hôtes des exoplanètes sont des acteurs clés dans la recherche de planètes potentiellement habitables. En effet, la luminosité, la température et la taille de l'étoile peuvent influencer la zone habitable d'une planète. Dans cette section, nous allons explorer l'influence des étoiles hôtes sur les exoplanètes.
""")

# Sélection du système stellaire
system_choice = st.selectbox("Choisissez un système stellaire :", options=host_names)

# Filtrer les données en fonction du système stellaire sélectionné
if system_choice == 'Tous les systèmes':
    filtered_data = data
else:
    filtered_data = data[data['Planet Host'] == system_choice]

# Checkbox pour afficher les planètes dans la zone habitable
show_goldilock_zone = st.checkbox("Afficher les planètes dans la zone habitable")

# Filtrer les données pour les planètes dans la zone habitable si l'option est cochée
if show_goldilock_zone:
    filtered_data['In Goldilock Zone'] = filtered_data['In Goldilock Zone'].astype(int)
    filtered_data = filtered_data[filtered_data['In Goldilock Zone'] == 1]

# Filtrer les données pour les planètes avec une excentricité inférieure à 0.6
filtered_data.loc[filtered_data["Eccentricity"] > 0.6, "In Goldilock Zone"] = 0

# Créer une nouvelle colonne pour la couleur des barres
filtered_data['Color'] = filtered_data['In Goldilock Zone'].apply(lambda x: 'In Goldilock Zone' if x == 1 else 'Other Exoplanets')

# Affichage du système stellaire sélectionné
st.write(f"Système stellaire sélectionné : **{system_choice}**")


# GRAPH 1
st.header("Distribution du type d'Étoile Hôte")
# Graphique de distribution des types d'étoiles hôtes
fig_host_types = px.histogram(filtered_data, x='Spectral Type',
                              title='Distribution des Types Spectraux des Étoiles Hôtes',
                              color='Color',
                              color_discrete_map={'In Goldilock Zone': 'yellow', 'Other Exoplanets': 'lightskyblue'})
st.plotly_chart(fig_host_types)

st.write("""
Ce graphique montre la distribution des types spectraux des étoiles hôtes des exoplanètes, ce qui est important car les étoiles de différents types peuvent avoir des caractéristiques différentes, telles que la taille, la température et la luminosité. Les étoiles plus massives et plus chaudes peuvent avoir des effets significatifs sur les exoplanètes qui les entourent, modifiant ainsi leur habitabilité potentielle.
""")

# GRAPH 2
st.header("Influence des Étoiles Hôtes")
# Graphique de distribution des températures des étoiles hôtes

fig_stellar_temp = px.histogram(filtered_data[filtered_data["Stellar Effective Temperature"] <= 15000], x='Stellar Effective Temperature',
                                title='Distribution des Températures des Étoiles Hôtes', color='Color',
                                color_discrete_map={'In Goldilock Zone': 'yellow', 'Other Exoplanets': 'lightskyblue'})
st.plotly_chart(fig_stellar_temp)

st.write("""
Ce graphique montre comment les températures des étoiles hôtes varient, ce qui est crucial car cela influence les zones habitables de leurs systèmes planétaires. Les étoiles plus chaudes ou plus froides peuvent avoir des effets significatifs sur les conditions des exoplanètes qui les entourent, modifiant ainsi leur habitabilité potentielle.
""")