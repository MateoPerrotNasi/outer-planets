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

# Titre de la section
st.title("🕰️ Découverte des exoplanètes")

# Explication de la Goldilock Zone
st.header("Quand et comment les Exoplanètes ont-elles été découvertes ?")
st.write("Les exoplanètes ont été découvertes a des époques différentes et avec des technologies différentes.\nVoici des graphiques illustrants cette idée.")

# Liste des noms d'hôtes uniques et option "Tous les systèmes"
host_names = ['Tous les systèmes'] + list(data['Planet Host'].unique())

# Sélection du système stellaire
system_choice = st.selectbox("Choisissez un système stellaire :", options=host_names)

# Filtrer les données en fonction du système stellaire sélectionné
if system_choice == 'Tous les systèmes':
    filtered_data = data
else:
    filtered_data = data[data['Planet Host'] == system_choice]


# GRAPH 1
st.header("Chronologie des Découvertes")
# Conversion de la colonne de date en format datetime si ce n'est pas déjà fait
filtered_data['Discovery Year'] = pd.to_datetime(filtered_data['Discovery Year'], format='%Y', errors='coerce')

st.write("""
Ce graphique permet de visualiser comment le nombre de découvertes d'exoplanètes a augmenté au fil des années, en mettant en évidence les avancées technologiques et les méthodes de détection telles que la méthode des transits et la méthode de la vitesse radiale. Les pics peuvent correspondre à des missions spatiales spécifiques ou à des améliorations dans les instruments de détection.
""")
# Conversion de la colonne de date en format datetime si ce n'est pas déjà fait
filtered_data['Discovery Year'] = pd.to_datetime(filtered_data['Discovery Year'], format='%Y', errors='coerce')

fig = px.histogram(filtered_data, x='Discovery Year', title='Années de découverte')
st.plotly_chart(fig)

# GRAPH 2
st.header("Méthodes de Découvertes")

st.write("""
Ce graphique permet de visualiser comment les méthodes de découvertes ayant permit de découvrir le plus de planète.
""")

method_counts = filtered_data['Discovery Method'].value_counts().reset_index()
method_counts.columns = ['Discovery Method', 'Count']
fig = px.pie(method_counts, values='Count', names='Discovery Method', title='Méthodes de découverte')
st.plotly_chart(fig)
