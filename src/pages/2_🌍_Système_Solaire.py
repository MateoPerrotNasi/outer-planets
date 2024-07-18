import streamlit as st
import pandas as pd
import plotly.express as px

# Chargement des données
data_path = './data/solar_system.csv'
data = pd.read_csv(data_path)

# Configuration de la page Streamlit
st.set_page_config(page_title="Outer Planets", page_icon="🪐", layout="wide")

# Sidebar avec logo
st.sidebar.image("./OP-logo-2.png", use_column_width=True)

# Titre
st.title("🌍 Système Solaire")

# Introduction sur les zones habitables
st.header("Exploration des Zones Habitables dans le Système Solaire")
st.write("""
Le système solaire est notre propre système planétaire composé du Soleil, des huit planètes et de nombreux autres objets célestes. Dans cette section, nous allons explorer les caractéristiques des planètes du système solaire et déterminer les planètes qui pourraient être dans la zone habitable.
""")

st.write(data.head())

# Visualisation de la distance des planètes par rapport au Soleil
st.subheader("Distance des Planètes par Rapport au Soleil")
fig_distance = px.bar(data, x='Planet Name', y='Orbit Semi-Major Axis',
                      labels={'Orbit Semi-Major Axis': 'Axe Semi-Majeur de l\'Orbite (UA)', 'Planet Name': 'Planète'},
                      title='Distance des Planètes par Rapport au Soleil')
st.plotly_chart(fig_distance)

# Visualisation des températures d'équilibre des planètes
st.subheader("Températures d'Équilibre des Planètes")
fig_temperature = px.bar(data, x='Planet Name', y='Equilibrium Temperature',
                         labels={'Equilibrium Temperature': 'Température d\'Équilibre (K)', 'Planet Name': 'Planète'},
                         title='Températures d\'Équilibre des Planètes du Système Solaire')
st.plotly_chart(fig_temperature)

# Visualisation du flux d'insolation des planètes
st.subheader("Flux d'Insolation des Planètes")
fig_insolation = px.bar(data, x='Planet Name', y='Insolation Flux',
                        labels={'Insolation Flux': 'Flux d\'Insolation (W/m^2)', 'Planet Name': 'Planète'},
                        title='Flux d\'Insolation des Planètes du Système Solaire')
st.plotly_chart(fig_insolation)

# Déterminer les planètes dans la zone habitable
data['In Goldilock Zone'] = data.apply(
    lambda row: 1 if row['Orbit Semi-Major Axis'] >= 0.95 and row['Orbit Semi-Major Axis'] <= 1.37 else 0, axis=1)
goldilocks_planets = data[data['In Goldilock Zone'] == 1]

# Afficher les planètes dans la Goldilock Zone
st.subheader("Planètes dans la Zone Habitable")
st.write(goldilocks_planets[['Planet Name', 'Orbit Semi-Major Axis', 'Equilibrium Temperature', 'Insolation Flux']])

# Visualisation des planètes dans la Goldilock Zone
fig_goldilocks = px.scatter(data, x='Orbit Semi-Major Axis', y='Equilibrium Temperature',
                            color='In Goldilock Zone', color_discrete_map={1: 'green', 0: 'red'},
                            labels={'Orbit Semi-Major Axis': 'Axe Semi-Majeur de l\'Orbite (UA)',
                                    'Equilibrium Temperature': 'Température d\'Équilibre (K)'},
                            title='Planètes du Système Solaire dans la Zone Habitable')
fig_goldilocks.add_vline(x=0.95, line_dash="dash", line_color="blue", annotation_text="Limite intérieure de la zone habitable")
fig_goldilocks.add_vline(x=1.37, line_dash="dash", line_color="orange", annotation_text="Limite extérieure de la zone habitable")
st.plotly_chart(fig_goldilocks)

# Conclusion
st.write("""
En conclusion, cette exploration des zones habitables dans notre propre système solaire révèle les conditions qui pourraient permettre la vie telle que nous la connaissons. 
Bien que notre Terre soit actuellement la seule planète connue pour abriter la vie, cette analyse met en lumière l'importance des zones habitables et de la recherche continue pour découvrir 
d'autres mondes potentiellement habitables au-delà de notre système solaire.
""")