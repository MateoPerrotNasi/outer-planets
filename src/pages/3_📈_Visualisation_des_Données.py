import streamlit as st
import pandas as pd
import plotly.express as px

# Chargement des données
data_path = './data/all_exoplanets_with_goldilock_zone.csv'
data = pd.read_csv(data_path)

# Configuration de la page Streamlit
st.set_page_config(page_title="Outer Planets", page_icon="🪐", layout="wide")

# Sidebar avec logo
st.sidebar.image("./OP-logo-2.png", use_column_width=True)

# Tableau des systèmes stellaires et le nombre de planètes
system_counts = data['Planet Host'].value_counts().reset_index()
system_counts.columns = ['Planet Host', 'Nombre de Planètes']

# Afficher uniquement les 5 premiers systèmes stellaires pour la sélection initiale
top_systems = system_counts.head(5)
st.header("Systèmes Stellaires et Nombre de Planètes")
st.write("""
Voici un tableau indiquant les systèmes stellaires et le nombre de planètes qu'ils comprennent.
""")
st.table(top_systems)

# Liste des noms d'hôtes uniques et option "Tous les systèmes"
host_names = ['Tous les systèmes'] + list(data['Planet Host'].unique())

st.header("📈 Visualisation des Données")
st.write(f"""
Explorez les relations entre différentes caractéristiques des exoplanètes à l'aide de graphiques interactifs.
Découvrez comment les exoplanètes sont découvertes, où elles se trouvent, et comment elles sont liées à leurs étoiles hôtes.
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


# Fonction pour mapper les couleurs en fonction du nom de l'hôte de la planète
def get_color(host_name):
    if host_name == 'Sun':
        return 'yellow'  # Couleur pour le système solaire
    else:
        return 'blue'  # Couleur par défaut pour les autres systèmes


# Ajouter une colonne 'Color' basée sur le nom de l'hôte de la planète
filtered_data['Color'] = filtered_data['Planet Host'].apply(get_color)

# Affichage du système stellaire sélectionné
st.write(f"Système stellaire sélectionné : **{system_choice}**")

# GRAPH 1
st.header("Chronologie des Découvertes")
# Conversion de la colonne de date en format datetime si ce n'est pas déjà fait
filtered_data['Discovery Year'] = pd.to_datetime(filtered_data['Discovery Year'], format='%Y', errors='coerce')

# Agrégation par année et comptage des découvertes
discovery_timeline = filtered_data.groupby(filtered_data['Discovery Year'].dt.year).size().reset_index(name='Nombre de Découvertes')

# Création du graphique avec Plotly Express
fig_timeline = px.line(discovery_timeline, x='Discovery Year', y='Nombre de Découvertes',
                       title='Nombre de Découvertes d\'Exoplanètes par Année')
st.plotly_chart(fig_timeline)

st.write("""
Ce graphique permet de visualiser comment le nombre de découvertes d'exoplanètes a augmenté au fil des années, en mettant en évidence les avancées technologiques et les méthodes de détection telles que la méthode des transits et la méthode de la vitesse radiale. Les pics peuvent correspondre à des missions spatiales spécifiques ou à des améliorations dans les instruments de détection.
""")

# GRAPH 2
st.header("Analyse des Caractéristiques des Exoplanètes")
# Filtrer les données pour les planètes dans la zone habitable si l'option est cochée
if show_goldilock_zone:
    filtered_data['In Goldilock Zone'] = filtered_data['In Goldilock Zone'].astype(int)
    filtered_data = filtered_data[filtered_data['In Goldilock Zone'] == 1]

# Widget slider pour permettre à l'utilisateur de spécifier une limite supérieure pour les périodes orbitales
max_orbital_period = st.slider("Limite supérieure pour les périodes orbitales (jours) :",
                               min_value=0, max_value=200000, value=200000)

# Filtrer les données pour les périodes orbitales inférieures ou égales à la limite supérieure spécifiée
filtered_orbital_data = filtered_data[filtered_data['Orbital Period Days'] <= max_orbital_period]

# Graphique de distribution des périodes orbitales avec la plage spécifiée par l'utilisateur
fig_orbital_periods = px.histogram(filtered_orbital_data, x='Orbital Period Days',
                                   title=f'Distribution des Périodes Orbitales des Exoplanètes (jusqu\'à {max_orbital_period} jours)')
st.plotly_chart(fig_orbital_periods)

st.write("""
Ce graphique montre comment sont réparties les périodes orbitales des exoplanètes, fournissant des insights sur la diversité des systèmes planétaires découverts. Les périodes orbitales peuvent varier de quelques jours à plusieurs années, ce qui peut indiquer la distance des exoplanètes par rapport à leur étoile hôte et leurs conditions orbitales.
""")

# GRAPH 4
st.header("Influence des Étoiles Hôtes")
# Graphique de distribution des températures des étoiles hôtes
fig_stellar_temp = px.histogram(filtered_data, x='Stellar Effective Temperature',
                                title='Distribution des Températures des Étoiles Hôtes')
st.plotly_chart(fig_stellar_temp)

st.write("""
Ce graphique montre comment les températures des étoiles hôtes varient, ce qui est crucial car cela influence les zones habitables de leurs systèmes planétaires. Les étoiles plus chaudes ou plus froides peuvent avoir des effets significatifs sur les conditions des exoplanètes qui les entourent, modifiant ainsi leur habitabilité potentielle.
""")

# GRAPH 5
st.header("Distances et Observabilité")
# Graphique de distribution des distances des exoplanètes
fig_distances = px.histogram(filtered_data, x='Orbit Semi-Major Axis',
                             title='Distribution des Distances des Exoplanètes')
st.plotly_chart(fig_distances)

st.write("""
Ce graphique montre la distribution des distances des exoplanètes en UA, illustrant les défis d'observation associés à ces distances. Les exoplanètes plus proches sont souvent plus faciles à étudier en détail, tandis que celles plus éloignées nécessitent des techniques d'observation plus avancées.
""")

# GRAPH 6
# Exemple spécifique de l'exoplanète Kepler-186 f
planet_data = filtered_data[filtered_data['Planet Name'] == 'Kepler-186 f']

st.header("Cas d'Étude : Kepler-186 f")
st.write("""
Kepler-186 f est une exoplanète située dans la zone habitable de son étoile hôte, Kepler-186. 
Elle a été découverte par le télescope spatial Kepler en 2014 et représente un cas intéressant 
pour l'étude des exoplanètes potentiellement habitables.
""")
st.write(planet_data)







# # GRAPH : Nombre de découvertes par an
# discovery_per_year = filtered_data['Discovery Year'].value_counts().sort_index().reset_index()
# discovery_per_year.columns = ['Year', 'Count']
#
# st.header("Évolution du nombre de découvertes par an")
# st.write("""
# Ce graphique montre comment le nombre d'exoplanètes découvertes a évolué au fil des années.
# Survolez une barre pour voir plus d'informations.
# """)
#
# fig = px.bar(
#     discovery_per_year,
#     x='Year',
#     y='Count',
#     labels={'Year': 'Année', 'Count': 'Nombre de Découvertes'},
#     title='Nombre de Découvertes d\'Exoplanètes par Année',
# )
#
# st.plotly_chart(fig)
#
# st.write("""
# #### Événements Importants :
# **2014** :
# - **Mission Kepler** : Le télescope spatial Kepler de la NASA, lancé en 2009, a découvert des milliers d'exoplanètes grâce à sa méthode de transit, qui détecte les diminutions de luminosité des étoiles causées par le passage d'une planète devant elles. En 2014, de nombreuses données de Kepler ont été analysées, conduisant à la confirmation de nombreuses exoplanètes.
# - **K2 Mission** : Après que la mission principale de Kepler ait été compromise par une défaillance matérielle en 2013, la mission K2 a commencé en 2014. K2 a continué à utiliser le télescope pour rechercher des exoplanètes, en observant différentes régions du ciel.
# **2017** :
# - **Analyse continue des données Kepler** : La mission Kepler a continué à produire des découvertes grâce à l'analyse continue de ses données. L'énorme quantité de données collectées par Kepler nécessite des années d'analyse, et de nombreux systèmes planétaires ont été confirmés en 2017 à partir des données précédentes.
# - **Campagnes K2** : Les campagnes d'observation de K2 ont continué à découvrir de nouvelles exoplanètes. Chaque campagne d'observation cible une région différente du ciel, permettant la découverte de nombreux nouveaux systèmes planétaires.
# """)
#
# # GRAPH : Période Orbitale vs. Masse de la Planète
# st.header("Période Orbitale vs. Masse de la Planète")
# st.write("""
# Ce graphique permet d'explorer la relation entre la période orbitale d'une exoplanète et sa masse.
# Il aide à identifier s'il existe des tendances ou des regroupements de planètes avec des périodes orbitales similaires et des masses comparables.
# """)
#
# fig1 = px.scatter(
#     filtered_data,
#     x='Orbital Period Days',
#     y='Mass',
#     color='Color',  # Utilisation de la colonne 'Color' pour différencier les couleurs
#     title='Période Orbitale vs. Masse de la Planète',
#     labels={'Orbital Period Days': 'Période Orbitale (jours)', 'Mass': 'Masse de l\'Exoplanète (Masse de Jupiter)'},
#     hover_name='Planet Name',
#     log_x=True,
#     log_y=True
# )
#
# st.plotly_chart(fig1)
#
# # GRAPH : Tendances des années de découverte
# st.header("Tendances des Années de Découverte")
# st.write("""
# Ce graphique montre l'évolution du nombre de découvertes d'exoplanètes au fil des ans.
# Il met en évidence les périodes de grande activité et permet de relier ces pics à des missions spécifiques ou à des avancées technologiques.
# """)
#
# fig2 = px.line(
#     discovery_per_year,
#     x='Year',
#     y='Count',
#     title='Nombre de Découvertes d\'Exoplanètes par Année',
#     labels={'Year': 'Année', 'Count': 'Nombre de Découvertes'},
#     markers=True
# )
#
# st.plotly_chart(fig2)
#
# # GRAPH : Répartition des méthodes de découverte
# discovery_method_counts = filtered_data['Discovery Method'].value_counts().reset_index()
# discovery_method_counts.columns = ['Discovery Method', 'Count']
#
# st.header("Répartition des Méthodes de Découverte des Exoplanètes")
# st.write("""
# Ce graphique illustre les différentes méthodes utilisées pour découvrir des exoplanètes et leur répartition.
# Il permet de comprendre quelles techniques ont été les plus efficaces ou les plus utilisées au fil du temps.
# """)
#
# fig3 = px.pie(
#     discovery_method_counts,
#     values='Count',
#     names='Discovery Method',
#     title='Répartition des Méthodes de Découverte des Exoplanètes',
#     hover_name='Discovery Method',
# )
#
# st.plotly_chart(fig3)
#
# # GRAPH : Évolution des Méthodes de Découverte des Exoplanètes par Année
# st.header("Évolution des Méthodes de Découverte des Exoplanètes par Année")
# st.write("""
# Ce graphique explore comment les méthodes de découverte ont évolué au fil des années.
# Il permet d'observer les changements de préférences ou d'efficacité des différentes méthodes utilisées pour découvrir des exoplanètes.
# """)
#
# fig4 = px.sunburst(
#     filtered_data,
#     path=['Discovery Year', 'Discovery Method'],
#     title='Évolution des Méthodes de Découverte des Exoplanètes par Année',
# )
#
# st.plotly_chart(fig4)
#
# # GRAPH : Caractéristiques Planétaires
# st.header("Caractéristiques Planétaires")
# st.write("""
# Ces graphiques permettent d'analyser les caractéristiques physiques des exoplanètes.
# Ils aident à identifier des corrélations potentielles entre différentes propriétés des planètes, comme la masse, le rayon, le demi-grand axe et le flux de l'insolation.
# """)
#
# # GRAPH : Masse vs. Rayon de l'Étoile Hôte
# fig5 = px.scatter(
#     filtered_data,
#     x='Mass',
#     y='Stellar Radius',
#     title='Masse vs. Rayon de l\'Étoile Hôte',
#     labels={'Mass': 'Masse de l\'Exoplanète (Masse de Jupiter)',
#             'Stellar Radius': 'Rayon de l\'Étoile Hôte (Rayon Solaire)'},
#     hover_name='Planet Name',
#     log_x=True,
#     log_y=True
# )
#
# st.plotly_chart(fig5)
#
# # GRAPH : Demi-grand axe vs. Flux de l'insolation
# fig6 = px.scatter(
#     filtered_data,
#     x='Orbit Semi-Major Axis',
#     y='Insolation Flux',
#     title='Demi-grand axe vs. Flux de l\'insolation',
#     labels={'Orbit Semi-Major Axis': 'Demi-grand axe (UA)', 'Insolation Flux': 'Flux de l\'insolation (W/m²)'},
#     hover_name='Planet Name',
#     log_x=True,
#     log_y=True
# )
#
# st.plotly_chart(fig6)
#
# # GRAPH : Corrélation entre la Masse des Exoplanètes et leur Température d'Équilibre
# st.header("Corrélation entre la Masse des Exoplanètes et leur Température d'Équilibre")
# st.write("""
# Ce graphique explore la relation entre la masse des exoplanètes et leur température d'équilibre.
# Il permet d'identifier des tendances et de mieux comprendre comment la masse peut influencer la température de surface des exoplanètes.
# """)
#
# fig7 = px.scatter(
#     filtered_data,
#     x='Mass',
#     y='Equilibrium Temperature',
#     title='Corrélation entre la Masse des Exoplanètes et leur Température d\'Équilibre',
#     labels={'Mass': 'Masse de l\'Exoplanète (Masse de Jupiter)',
#             'Equilibrium Temperature': 'Température d\'Équilibre (K)'},
#     hover_name='Planet Name',
# )
#
# st.plotly_chart(fig7)
#
# # GRAPH : Relation entre la Métallicité Stellaire et le Rayon de l'Étoile Hôte
# st.header("Relation entre la Métallicité Stellaire et le Rayon de l'Étoile Hôte")
# st.write("""
# Ce graphique examine la relation entre la métallicité stellaire et le rayon des étoiles hôtes.
# Il aide à comprendre comment la composition chimique des étoiles peut influencer leur taille.
# """)
#
# fig8 = px.scatter(
#     filtered_data,
#     x='Stellar Metallicity',
#     y='Stellar Radius',
#     title='Relation entre la Métallicité Stellaire et le Rayon de l\'Étoile Hôte',
#     labels={'Stellar Metallicity': 'Métallicité Stellaire', 'Stellar Radius': 'Rayon Stellaire (Rayon Solaire)'},
#     hover_name='Planet Host',
# )
#
# st.plotly_chart(fig8)
#
# # GRAPH : Répartition des Types Spectraux des Étoiles Hôtes
# spectral_type_counts = filtered_data['Spectral Type'].value_counts().reset_index()
# spectral_type_counts.columns = ['Spectral Type', 'Count']
#
# st.header("Répartition des Types Spectraux des Étoiles Hôtes")
# st.write("""
# Ce graphique montre la distribution des types spectraux des étoiles hôtes des exoplanètes.
# Il permet de voir quels types d'étoiles sont les plus courants parmi celles qui hébergent des exoplanètes.
# """)
#
# fig9 = px.bar(
#     spectral_type_counts,
#     x='Spectral Type',
#     y='Count',
#     title='Répartition des Types Spectraux des Étoiles Hôtes',
#     labels={'Spectral Type': 'Type Spectral', 'Count': 'Nombre d\'Étoiles'},
# )
#
# st.plotly_chart(fig9)

st.write("---")
st.write(
    "Projet réalisé par PERROT--NASI Matéo et TOMATIS Margot. Pour plus d'informations, vous pouvez nous retrouver sur nos github.")
