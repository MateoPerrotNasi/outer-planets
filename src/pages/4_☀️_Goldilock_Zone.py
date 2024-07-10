import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

# Chargement des données
data_path = './data/all_exoplanets_2021.csv'
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


# Fonction pour calculer la zone habitable
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

# Application de la fonction à chaque ligne du DataFrame
data['In Goldilock Zone'] = data.apply(is_in_goldilock_zone, axis=1)

# Affichage des premières lignes pour vérifier
st.write(data.head())

# Sauvegarder le DataFrame modifié si nécessaire
data.to_csv('./data/all_exoplanets_with_goldilock_zone.csv', index=False)

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
cleaned_data = data.dropna(subset=['Orbital Period Days', 'Orbit Semi-Major Axis', 'Insolation Flux', 'Equilibrium Temperature', 'Stellar Effective Temperature', 'Stellar Radius', 'Stellar Mass']).copy()

# Supprimer la colonne 'Cluster' si elle existe déjà
if 'Cluster' in cleaned_data.columns:
    cleaned_data.drop(columns=['Cluster'], inplace=True)

# Ajouter la nouvelle colonne 'Cluster'
cleaned_data['Cluster'] = clusters

# Explication des Clusters
st.write("""
## Analyse des Clusters
Les clusters permettent de regrouper les exoplanètes en fonction de leurs caractéristiques orbitales et stellaires. Chaque cluster peut potentiellement représenter une catégorie distincte d'exoplanètes avec des propriétés similaires. Par exemple, un cluster pourrait regrouper des planètes proches de leur étoile avec des périodes orbitales courtes, tandis qu'un autre cluster pourrait regrouper des planètes plus éloignées avec des périodes orbitales plus longues et des températures d'équilibre plus basses.
""")

# Visualisation des clusters
st.write("""
### Graphique 1 : Distribution des Clusters selon l'Axe Semi-Majeur et la Température d'Équilibre
Ce graphique montre comment les exoplanètes sont réparties en différents clusters selon leur axe semi-majeur et leur température d'équilibre. Cela permet d'identifier les groupes d'exoplanètes avec des propriétés similaires en termes de distance par rapport à leur étoile et de température.
""")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='Orbit Semi-Major Axis', y='Equilibrium Temperature', hue='Cluster', data=cleaned_data, palette='viridis', ax=ax)
plt.xlabel('Orbit Semi-Major Axis')
plt.ylabel('Equilibrium Temperature')
plt.title('Clustering des Exoplanètes')
st.pyplot(fig)

# Affichage des clusters en radar chart (facultatif)
st.write("""
### Graphique 2 : Radar Chart des Caractéristiques Moyennes des Clusters
Ce radar chart montre les caractéristiques moyennes des exoplanètes dans chaque cluster. Il permet de visualiser les différences entre les clusters en termes de température effective stellaire, de flux d'insolation, de période orbitale, etc.
""")
# Préparer les données pour radar chart
# Sélectionner uniquement les colonnes numériques
numeric_cols = cleaned_data.select_dtypes(include=[np.number]).columns.tolist()
cluster_means = cleaned_data.groupby('Cluster')[numeric_cols].mean().reset_index(drop=True)

fig_radar = px.line_polar(cluster_means, r='Stellar Effective Temperature', theta='Cluster', line_close=True)
st.plotly_chart(fig_radar)

# Visualisation avec Plotly
st.write("""
### Graphique 3 : Visualisation Interactive des Clusters avec Plotly
Ce graphique interactif permet d'explorer les clusters en survolant les points pour voir les détails des exoplanètes. Il montre la répartition des exoplanètes selon l'axe semi-majeur et la température d'équilibre, avec une coloration par cluster.
""")
fig_plotly = px.scatter(cleaned_data, x='Orbit Semi-Major Axis', y='Equilibrium Temperature', color='Cluster',
                        title='Clustering des Exoplanètes', labels={'Orbit Semi-Major Axis':'Orbit Semi-Major Axis', 'Equilibrium Temperature':'Equilibrium Temperature'})
st.plotly_chart(fig_plotly)

# Afficher les planètes dans la Goldilock Zone
goldilocks_data = cleaned_data[cleaned_data['In Goldilock Zone'] == 1]
st.header("Planètes dans la Goldilock Zone")
st.write(goldilocks_data[['Planet Name', 'Planet Host', 'Orbital Period Days', 'Orbit Semi-Major Axis', 'Insolation Flux', 'Equilibrium Temperature', 'Stellar Effective Temperature', 'Stellar Radius', 'Stellar Mass', 'Cluster']])

# Visualisation des planètes dans la Goldilock Zone
st.write("""
### Graphique 4 : Distribution des Planètes dans la Goldilock Zone selon les Clusters
Ce graphique montre la répartition des planètes situées dans la Goldilock Zone en fonction de leur axe semi-majeur et de leur température d'équilibre. Il permet d'identifier les clusters de planètes potentiellement habitables.
""")
fig_goldilocks, ax_goldilocks = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='Orbit Semi-Major Axis', y='Equilibrium Temperature', hue='Cluster', data=goldilocks_data, palette='coolwarm', ax=ax_goldilocks)
plt.xlabel('Orbit Semi-Major Axis')
plt.ylabel('Equilibrium Temperature')
plt.title('Planètes dans la Goldilock Zone')
st.pyplot(fig_goldilocks)
