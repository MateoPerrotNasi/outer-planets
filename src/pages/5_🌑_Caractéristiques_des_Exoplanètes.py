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

# Titre
st.title("🌑 Caractéristiques des Exoplanètes")

st.write("""
Les exoplanètes sont des planètes situées en dehors de notre système solaire. Elles peuvent être de tailles, de compositions et d'orbites très variées. Dans cette section, nous allons explorer les caractéristiques des exoplanètes découvertes à ce jour.
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
st.header("Analyse des Caractéristiques des Exoplanètes")
# Filtrer les données pour les planètes dans la zone habitable si l'option est cochée
if show_goldilock_zone:
    filtered_data['In Goldilock Zone'] = filtered_data['In Goldilock Zone'].astype(int)
    filtered_data = filtered_data[filtered_data['In Goldilock Zone'] == 1]

# Widget slider pour permettre à l'utilisateur de spécifier une limite supérieure pour les périodes orbitales
max_orbital_period = st.slider("Limite supérieure pour les périodes orbitales (jours) :",
                               min_value=0, max_value=50000, value=50000)

# Filtrer les données pour les périodes orbitales inférieures ou égales à la limite supérieure spécifiée
filtered_orbital_data = filtered_data[filtered_data['Orbital Period Days'] <= max_orbital_period]

# Graphique de distribution des périodes orbitales avec la plage spécifiée par l'utilisateur
fig_orbital_periods = px.histogram(filtered_orbital_data[filtered_orbital_data["Orbital Period Days"] <= 50000], x='Orbital Period Days',
                                   title=f'Distribution des Périodes Orbitales des Exoplanètes (jusqu\'à {max_orbital_period} jours)',
                                   color='Color',
                                   color_discrete_map={'In Goldilock Zone': 'yellow', 'Other Exoplanets': 'lightskyblue'})
st.plotly_chart(fig_orbital_periods)

st.write("""
Ce graphique montre comment sont réparties les périodes orbitales des exoplanètes, fournissant des insights sur la diversité des systèmes planétaires découverts. Les périodes orbitales peuvent varier de quelques jours à plusieurs années, ce qui peut indiquer la distance des exoplanètes par rapport à leur étoile hôte et leurs conditions orbitales.
""")

# GRAPH 2
st.header("Distances et Observabilité")
# Graphique de distribution des distances des exoplanètes
fig_distances = px.histogram(filtered_data[filtered_data["Orbit Semi-Major Axis"] <= 400], x='Orbit Semi-Major Axis',
                             title='Distribution des Distances des Exoplanètes', color='Color',
                             color_discrete_map={'In Goldilock Zone': 'yellow', 'Other Exoplanets': 'lightskyblue'})
st.plotly_chart(fig_distances)

st.write("""
Ce graphique montre la distribution des distances des exoplanètes en UA, illustrant les défis d'observation associés à ces distances. Les exoplanètes plus proches sont souvent plus faciles à étudier en détail, tandis que celles plus éloignées nécessitent des techniques d'observation plus avancées.
""")

# GRAPH 3
st.header("Distribution de l'excentricité")
# Graphique de distribution de l'excentricité des orbites des exoplanètes
fig_eccentricity = px.histogram(filtered_data, x='Eccentricity',
                                title='Distribution de l\'Excentricité des Orbites des Exoplanètes', color='Color',
                                color_discrete_map={'In Goldilock Zone': 'yellow', 'Other Exoplanets': 'lightskyblue'})

st.plotly_chart(fig_eccentricity)

# GRAPH 4
# Exemple spécifique de l'exoplanète Kepler-186 f
planet_data = filtered_data[filtered_data['Planet Name'] == 'Kepler-186 f']

st.header("Cas d'Étude : Kepler-186 f")
st.write("""
Kepler-186 f est une exoplanète située dans la zone habitable de son étoile hôte, Kepler-186. 
Elle a été découverte par le télescope spatial Kepler en 2014 et représente un cas intéressant 
pour l'étude des exoplanètes potentiellement habitables.
""")
st.write(planet_data)
