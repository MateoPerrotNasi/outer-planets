import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données
data_path = './data/solar_system.csv'
data = pd.read_csv(data_path)

# Configuration de la page Streamlit
st.set_page_config(page_title="Outer Planets", page_icon="🪐", layout="wide")

# Sidebar avec logo
st.sidebar.image("./OP-logo-2.png", use_column_width=True)

# Titre de la section
st.title("🌍 Système Solaire")

# Affichage des données
st.write(data)

# Graphique : Nombre de planètes par méthode de découverte
st.header('Nombre de planètes par méthode de découverte')

# Sélection de la méthode de découverte via un widget selectbox
discovery_methods = data['Discovery Method'].unique().tolist()
selected_method = st.selectbox('Sélectionnez une méthode de découverte', discovery_methods)

# Filtrage des données selon la méthode sélectionnée
filtered_data = data[data['Discovery Method'] == selected_method]
method_counts = filtered_data['Discovery Method'].value_counts()

# Affichage du nombre de planètes découvertes par méthode
st.subheader(f'Nombre de planètes découvertes avec la méthode "{selected_method}": {method_counts[selected_method]}')

# Graphique interactif : Température effective stellaire vs Température d'équilibre
st.header('Température effective stellaire vs Température d\'équilibre')

# Sélection d'une plage de température effective stellaire
temp_range = st.slider('Sélectionnez une plage de température effective stellaire (K)', int(data['Stellar Effective Temperature'].min()), int(data['Stellar Effective Temperature'].max()), (2000, 7000))

# Filtrage des données selon la plage de température sélectionnée
filtered_data_temp = data[(data['Stellar Effective Temperature'] >= temp_range[0]) & (data['Stellar Effective Temperature'] <= temp_range[1])]

# Affichage du nuage de points interactif
plt.figure(figsize=(10, 6))
scatterplot = sns.scatterplot(x='Stellar Effective Temperature', y='Equilibrium Temperature', data=filtered_data_temp, hue='Planet Name', palette='viridis', size='Distance', sizes=(20, 200))
plt.xlabel('Température effective stellaire (K)')
plt.ylabel('Température d\'équilibre (K)')
plt.title('Relation entre la température stellaire et la température d\'équilibre des planètes')
st.pyplot()

# Graphique interactif : Distribution de la période orbitale des planètes
st.header('Distribution de la période orbitale des planètes')

# Sélection du nombre de bins pour l'histogramme
num_bins = st.slider('Sélectionnez le nombre de bins pour l\'histogramme', min_value=10, max_value=50, value=20)

# Affichage de l'histogramme interactif
plt.figure(figsize=(10, 6))
histplot = sns.histplot(data['Orbital Period Days'], bins=num_bins, kde=True)
plt.xlabel('Période orbitale (jours)')
plt.ylabel('Nombre de planètes')
plt.title('Distribution de la période orbitale des planètes')
st.pyplot()
