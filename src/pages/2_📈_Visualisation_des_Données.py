import streamlit as st
import pandas as pd
import plotly.express as px

# Chargement des données
data_path = './data/all_exoplanets_2021.csv'
data = pd.read_csv(data_path)

# Configuration de la page Streamlit
st.set_page_config(page_title="Outer Planets", page_icon="🪐", layout="wide")

# Sidebar avec logo
st.sidebar.image("./OP-logo-2.png", use_column_width=True)

st.header("📈 Visualisation des Données")
st.write("""
Explorez les relations entre différentes caractéristiques des exoplanètes à l'aide de graphiques interactifs.
Découvrez comment les exoplanètes sont découvertes, où elles se trouvent, et comment elles sont liées à leurs étoiles hôtes.
""")

# GRAPH : Nombre de découvertes par an
discovery_per_year = data['Discovery Year'].value_counts().sort_index().reset_index()
discovery_per_year.columns = ['Year', 'Count']

st.header("Évolution du nombre de découvertes par an")
st.write("""
Ce graphique montre comment le nombre d'exoplanètes découvertes a évolué au fil des années.
Survolez une barre pour voir plus d'informations.
""")

messages = {
    2014: "- **Mission Kepler** : Le télescope spatial Kepler de la NASA, lancé en 2009, a découvert des milliers d'exoplanètes grâce à sa méthode de transit, qui détecte les diminutions de luminosité des étoiles causées par le passage d'une planète devant elles. En 2014, de nombreuses données de Kepler ont été analysées, conduisant à la confirmation de nombreuses exoplanètes.<br>"
          "- **K2 Mission** : Après que la mission principale de Kepler ait été compromise par une défaillance matérielle en 2013, la mission K2 a commencé en 2014. K2 a continué à utiliser le télescope pour rechercher des exoplanètes, en observant différentes régions du ciel.",
    2017: "- **Analyse continue des données Kepler** : La mission Kepler a continué à produire des découvertes grâce à l'analyse continue de ses données. L'énorme quantité de données collectées par Kepler nécessite des années d'analyse, et de nombreux systèmes planétaires ont été confirmés en 2017 à partir des données précédentes."
          "- **Campagnes K2** : Les campagnes d'observation de K2 ont continué à découvrir de nouvelles exoplanètes. Chaque campagne d'observation cible une région différente du ciel, permettant la découverte de nombreux nouveaux systèmes planétaires."
}

discovery_per_year['Message'] = discovery_per_year['Year'].map(messages).fillna("Aucun message spécifique pour cette année.")

fig = px.bar(
    discovery_per_year,
    x='Year',
    y='Count',
    # hover_data={'Year': True, 'Count': True, 'Message': discovery_per_year['Message']},
    labels={'Year': 'Année', 'Count': 'Nombre de Découvertes'},
    title='Nombre de Découvertes d\'Exoplanètes par Année',
)

st.plotly_chart(fig)

# GRAPH : Répartition des méthodes de découverte
st.header("Période Orbitale vs. Masse de la Planète")
st.write("""
Ce graphique permet d'explorer la relation entre la période orbitale d'une exoplanète et sa masse. 
Il aide à identifier s'il existe des tendances ou des regroupements de planètes avec des périodes orbitales similaires et des masses comparables.
""")

fig1 = px.scatter(
    data,
    x='Orbital Period Days',
    y='Mass',
    title='Période Orbitale vs. Masse de la Planète',
    labels={'Orbital Period Days': 'Période Orbitale (jours)', 'Mass': 'Masse de l\'Exoplanète (Masse de Jupiter)'},
    hover_name='Planet Name',
    log_x=True,
    log_y=True
)

st.plotly_chart(fig1)

# GRAPH : Tendances des annees de decouverte
st.header("Tendances des Années de Découverte")
st.write("""
Ce graphique montre l'évolution du nombre de découvertes d'exoplanètes au fil des ans. 
Il met en évidence les périodes de grande activité et permet de relier ces pics à des missions spécifiques ou à des avancées technologiques.
""")

fig2 = px.line(
    discovery_per_year,
    x='Year',
    y='Count',
    title='Nombre de Découvertes d\'Exoplanètes par Année',
    labels={'Year': 'Année', 'Count': 'Nombre de Découvertes'},
    markers=True
)

st.plotly_chart(fig2)

# GRAPH : repartition methodes de decouverte
discovery_method_counts = data['Discovery Method'].value_counts().reset_index()
discovery_method_counts.columns = ['Discovery Method', 'Count']

st.header("Répartition des Méthodes de Découverte des Exoplanètes")
st.write("""
Ce graphique illustre les différentes méthodes utilisées pour découvrir des exoplanètes et leur répartition.
Il permet de comprendre quelles techniques ont été les plus efficaces ou les plus utilisées au fil du temps.
""")

fig1 = px.pie(
    discovery_method_counts,
    values='Count',
    names='Discovery Method',
    title='Répartition des Méthodes de Découverte des Exoplanètes',
    hover_name='Discovery Method',
)

st.plotly_chart(fig1)

# GRAPH : Évolution des Méthodes de Découverte des Exoplanètes par Année
st.header("Évolution des Méthodes de Découverte des Exoplanètes par Année")
st.write("""
Ce graphique explore comment les méthodes de découverte ont évolué au fil des années.
Il permet d'observer les changements de préférences ou d'efficacité des différentes méthodes utilisées pour découvrir des exoplanètes.
""")

fig2 = px.sunburst(
    data,
    path=['Discovery Year', 'Discovery Method'],
    title='Évolution des Méthodes de Découverte des Exoplanètes par Année',
)

st.plotly_chart(fig2)

# GRAPH : Masse vs. Rayon, Demi-grand axe vs. Flux de l'insolation
st.header("Caractéristiques Planétaires")
st.write("""
Ces graphiques permettent d'analyser les caractéristiques physiques des exoplanètes.
Ils aident à identifier des corrélations potentielles entre différentes propriétés des planètes, comme la masse, le rayon, le demi-grand axe et le flux de l'insolation.
""")

fig3 = px.scatter(
    data,
    x='Mass',
    y='Stellar Radius',
    title='Masse vs. Rayon de l\'Étoile Hôte',
    labels={'Mass': 'Masse de l\'Exoplanète (Masse de Jupiter)', 'Stellar Radius': 'Rayon de l\'Étoile Hôte (Rayon Solaire)'},
    hover_name='Planet Name',
    log_x=True,
    log_y=True
)

st.plotly_chart(fig3)

# GRAPH : Demi-grand axe vs. Flux de l'insolation
fig4 = px.scatter(
    data,
    x='Orbit Semi-Major Axis',
    y='Insolation Flux',
    title='Demi-grand axe vs. Flux de l\'insolation',
    labels={'Orbit Semi-Major Axis': 'Demi-grand axe (UA)', 'Insolation Flux': 'Flux de l\'insolation (W/m²)'},
    hover_name='Planet Name',
    log_x=True,
    log_y=True
)

st.plotly_chart(fig4)

# GRAPH : Masse des Exoplanètes et leur Température d'Équilibre
st.header("Corrélation entre la Masse des Exoplanètes et leur Température d'Équilibre")
st.write("""
Ce graphique explore la relation entre la masse des exoplanètes et leur température d'équilibre.
Il permet d'identifier des tendances et de mieux comprendre comment la masse peut influencer la température de surface des exoplanètes.
""")

fig3 = px.scatter(
    data,
    x='Mass',
    y='Equilibrium Temperature',
    title='Corrélation entre la Masse des Exoplanètes et leur Température d\'Équilibre',
    labels={'Mass': 'Masse de l\'Exoplanète (Masse de Jupiter)', 'Equilibrium Temperature': 'Température d\'Équilibre (K)'},
    hover_name='Planet Name',
)

st.plotly_chart(fig3)

# GRAPH : Métallicité Stellaire et le Rayon de l'Étoile Hôte
st.header("Relation entre la Métallicité Stellaire et le Rayon de l'Étoile Hôte")
st.write("""
Ce graphique examine la relation entre la métallicité stellaire et le rayon des étoiles hôtes.
Il aide à comprendre comment la composition chimique des étoiles peut influencer leur taille.
""")

fig4 = px.scatter(
    data,
    x='Stellar Metallicity',
    y='Stellar Radius',
    title='Relation entre la Métallicité Stellaire et le Rayon de l\'Étoile Hôte',
    labels={'Stellar Metallicity': 'Métallicité Stellaire', 'Stellar Radius': 'Rayon Stellaire (Rayon Solaire)'},
    hover_name='Planet Host',
)

st.plotly_chart(fig4)

# GRAPH : Types Spectraux des Étoiles Hôtes
spectral_type_counts = data['Spectral Type'].value_counts().reset_index()
spectral_type_counts.columns = ['Spectral Type', 'Count']

st.header("Répartition des Types Spectraux des Étoiles Hôtes")
st.write("""
Ce graphique montre la distribution des types spectraux des étoiles hôtes des exoplanètes.
Il permet de voir quels types d'étoiles sont les plus courants parmi celles qui hébergent des exoplanètes.
""")

fig5 = px.bar(
    spectral_type_counts,
    x='Spectral Type',
    y='Count',
    title='Répartition des Types Spectraux des Étoiles Hôtes',
    labels={'Spectral Type': 'Type Spectral', 'Count': 'Nombre d\'Étoiles'},
)

st.plotly_chart(fig5)


st.write("---")
st.write("Projet réalisé par PERROT--NASI Matéo et TOMATIS Margot. Pour plus d'informations, vous pouvez nous retrouver sur nos github.")
