import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import plotly.express as px

# Chargement des données
data_path = './data/all_exoplanets_with_goldilock_zone.csv'
data = pd.read_csv(data_path)

# Configuration de la page Streamlit
st.set_page_config(page_title="Outer Planets", page_icon="🪐", layout="wide")

# Sidebar avec logo
st.sidebar.image("./OP-logo-2.png", use_column_width=True)

# Titre de la section
st.title("☀️ Goldilock Zone")

# Explication de la Goldilock Zone
st.header("Qu'est-ce que la Goldilock Zone ?")
st.write("""
La Goldilock Zone, ou zone habitable, est la région autour d'une étoile où les conditions peuvent être juste comme il faut pour permettre l'existence de l'eau liquide à la surface d'une planète. Cette zone n'est ni trop chaude ni trop froide, mais juste à la bonne distance pour que l'eau ne s'évapore pas complètement ni ne gèle. L'existence d'eau liquide est considérée comme l'une des conditions essentielles pour la vie telle que nous la connaissons.
""")

# Affichage des premières lignes pour vérifier
st.write(data.head())

# Nombre de planetes dans la Goldilock Zone
num_goldilocks = data['In Goldilock Zone'].sum()
total_planets = len(data)
st.write(f"Nombre de planètes dans la Goldilock Zone : {num_goldilocks} sur {total_planets} ({num_goldilocks/total_planets:.2%})")

# Calcul de la Goldilock Zone
st.header("Calcul de la Goldilock Zone")
st.write("""
```python
def is_in_goldilock_zone(row):
    T_star = row['Stellar Effective Temperature']  # Température effective de l'étoile
    R_star = row['Stellar Radius']  # Rayon stellaire
    a_planet = row['Orbit Semi-Major Axis']  # Axe semi-major de l'orbite de la planète

    if pd.isna(T_star) or pd.isna(R_star) or pd.isna(a_planet):
        return 0

    # Calcul de la luminosité stellaire en unités solaires
    T_sun = 5778  # Température effective du Soleil en Kelvin
    L_star = (R_star**2) * ((T_star / T_sun)**4)

    # Calcul des distances de la zone habitable
    inner_hz = np.sqrt(L_star) * 0.75
    outer_hz = np.sqrt(L_star) * 1.77

    # Vérification si la planète est dans la zone habitable
    return 1 if inner_hz <= a_planet <= outer_hz else 0
```
""")

# Visualisation des Données de la Goldilock Zone
st.header("Visualisation des Données de la Goldilock Zone")

# Clustering
st.header("Analyse de Clustering des Exoplanètes")

# Sélection des caractéristiques pertinentes pour le clustering
features = data[['Orbital Period Days', 'Orbit Semi-Major Axis', 'Insolation Flux', 'Equilibrium Temperature', 'Stellar Effective Temperature', 'Stellar Radius', 'Stellar Mass']]

# Nettoyage des données
features_cleaned = features.dropna()

# Normalisation des données
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features_cleaned)

# Application de K-means
kmeans = KMeans(n_clusters=5)
clusters = kmeans.fit_predict(scaled_features)

# Création d'un DataFrame pour les données nettoyées et normalisées
cleaned_data = data.dropna(subset=features_cleaned.columns).copy()

# Supprimer la colonne 'Cluster' si elle existe déjà
if 'Cluster' in cleaned_data.columns:
    cleaned_data.drop(columns=['Cluster'], inplace=True)

# Ajouter la nouvelle colonne 'Cluster'
cleaned_data['Cluster'] = clusters

# Explication des Clusters
st.write("""
Les clusters permettent de regrouper les exoplanètes en fonction de leurs caractéristiques orbitales et stellaires. Chaque cluster peut potentiellement représenter une catégorie distincte d'exoplanètes avec des propriétés similaires. Par exemple, un cluster pourrait regrouper des planètes proches de leur étoile avec des périodes orbitales courtes, tandis qu'un autre cluster pourrait regrouper des planètes plus éloignées avec des périodes orbitales plus longues et des températures d'équilibre plus basses.
""")

# Visualisation des clusters avec Plotly
st.write("""
### Visualisation Interactive des Clusters avec Plotly
Ce graphique interactif permet d'explorer les clusters en survolant les points pour voir les détails des exoplanètes. Il montre la répartition des exoplanètes selon l'axe semi-majeur et la température d'équilibre, avec une coloration par cluster.
""")
fig_plotly = px.scatter(cleaned_data, x='Orbit Semi-Major Axis', y='Equilibrium Temperature', color='Cluster',
                        title='Clustering des Exoplanètes', labels={'Orbit Semi-Major Axis':'Orbit Semi-Major Axis', 'Equilibrium Temperature':'Equilibrium Temperature'})
st.plotly_chart(fig_plotly)

# Afficher les planètes dans la Goldilock Zone
goldilocks_data = cleaned_data[cleaned_data['In Goldilock Zone'] == 1]
st.header("Planètes dans la Goldilock Zone")
st.write(goldilocks_data[['Planet Name', 'Planet Host', 'Orbital Period Days', 'Orbit Semi-Major Axis', 'Insolation Flux', 'Equilibrium Temperature', 'Stellar Effective Temperature', 'Stellar Radius', 'Stellar Mass', 'Cluster']])

# Visualisation des planètes dans la Goldilock Zone avec Plotly
st.write("""
### Distribution des Planètes dans la Goldilock Zone selon les Clusters
Ce graphique montre la répartition des planètes situées dans la Goldilock Zone en fonction de leur axe semi-majeur et de leur température d'équilibre. Il permet d'identifier les clusters de planètes potentiellement habitables.
""")
fig_goldilocks = px.scatter(goldilocks_data, x='Orbit Semi-Major Axis', y='Equilibrium Temperature', color='Cluster',
                            title='Planètes dans la Goldilock Zone', labels={'Orbit Semi-Major Axis':'Orbit Semi-Major Axis', 'Equilibrium Temperature':'Equilibrium Temperature'})
st.plotly_chart(fig_goldilocks)
