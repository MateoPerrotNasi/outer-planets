import streamlit as st


# Define the content for the Data page
def data():
    st.title("Données sur les Exoplanètes")

    st.markdown("## Qu'est-ce qu'une zone habitable (Goldilocks zone) ?")
    st.write("""
    Une zone habitable (Goldilocks zone) est une région autour d'une étoile où les conditions sont idéales pour qu'une planète puisse potentiellement abriter de l'eau liquide à sa surface. 
    Une planète située dans une zone habitable a plus de chances d'abriter de la vie que celles situées en dehors de cette zone.
    """)

    st.markdown("## Quelles sont les caractéristiques des exoplanètes ?")
    st.write("""
    Les caractéristiques des exoplanètes comprennent :
    - La **masse** de l'exoplanète
    - Le **rayon** de l'exoplanète
    - La **température** de l'exoplanète
    - La **distance** de l'exoplanète par rapport à son étoile
    - La **luminosité** de l'étoile
    - La **durée de l'orbite** de l'exoplanète
    - Le **nombre de planètes** dans le système
    - Le **nombre d'étoiles** dans le système
    """)

    st.markdown("## Quelles sont les données utilisées pour ce projet ?")
    st.write("""
    Les données utilisées pour ce projet proviennent du [Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/). 
    Ce site a été créé par le California Institute of Technology (Caltech) et la NASA, et toutes les données sont publiques, fiables et vérifiées.
    Les données comprennent les caractéristiques des exoplanètes découvertes par plusieurs laboratoires. 
    Nous utilisons les données de 2021, car elles sont actuellement les plus fiables, complètes et nettoyées.

    Le jeu de données compte 4575 lignes et 23 colonnes. Elles sont régulièrement mises à jour et comprennent les caractéristiques suivantes :

    - **No**: Numéro d'identification unique attribué à chaque exoplanète dans la base de données.
    - **Planet Name**: Nom de l'exoplanète
    - **Planet Host**: Nom de l'étoile autour de laquelle l'exoplanète orbite.
    - **Num Stars**: Nombre d'étoiles dans le système
        > Certaines exoplanètes orbitent autour de systèmes avec plusieurs étoiles.
    - **Num Planets**: Nombre de planètes dans le système
    - **Discovery Method**: Méthode de découverte de l'exoplanète
        > La technique utilisée pour découvrir l'exoplanète, comme le transit, la vitesse radiale, ou l'imagerie directe.
    - **Discovery Year**: Année de découverte de l'exoplanète
    - **Discovery Facility**: Laboratoire de recherche ayant découvert l'exoplanète
    - **Orbital Period Days**: Durée de l'orbite de l'exoplanète en jours
        > Le temps que met l'exoplanète pour faire un tour complet autour de son étoile, mesuré en jours terrestres.
    - **Orbit Semi-Major Axis**: Demi-grand axe de l'orbite de l'exoplanète en UA
        > La distance moyenne entre l'exoplanète et son étoile, mesurée en unités astronomiques (1 UA est la distance moyenne entre la Terre et le Soleil).
    - **Mass**: Masse de l'exoplanète en masse de Jupiter
        > La masse de l'exoplanète comparée à celle de Jupiter. Par exemple, une planète ayant une masse de 1 masse de Jupiter a la même masse que Jupiter.
    - **Eccentricity**: Excentricité de l'orbite de l'exoplanète
        > Une mesure de la forme de l'orbite de l'exoplanète. Une excentricité de 0 signifie une orbite parfaitement circulaire, tandis qu'une excentricité proche de 1 indique une orbite très allongée.
    - **Insolation Flux**: Flux d'insolation de l'exoplanète en W/m²
        > La quantité d'énergie reçue par l'exoplanète de la part de son étoile, mesurée en watts par mètre carré.
    - **Equilibrium Temperature**: Température d'équilibre de l'exoplanète en K
        > La température que l'exoplanète atteindrait si elle absorbait et réémettait l'énergie de son étoile de manière uniforme, mesurée en kelvins.
    - **Spectral Type**: Type spectral de l'étoile hôte
        > La classification de l'étoile hôte basée sur sa température de surface et sa couleur. Par exemple, le Soleil est de type spectral G2.
    - **Stellar Effective Temperature**: Température effective de l'étoile hôte en K
        > La température de surface de l'étoile hôte, mesurée en kelvins.
    - **Stellar Radius**: Rayon de l'étoile hôte en rayon solaire
        > La taille de l'étoile hôte comparée à celle du Soleil. Un rayon de 1 signifie que l'étoile est de la même taille que le Soleil.
    - **Stellar Mass**: Masse de l'étoile hôte en masse solaire
        > La masse de l'étoile hôte comparée à celle du Soleil. Une masse de 1 signifie que l'étoile a la même masse que le Soleil.
    - **Stellar Metallicity**: Métallicité de l'étoile hôte
        > La proportion de l'étoile constituée d'éléments plus lourds que l'hydrogène et l'hélium. Une métallicité élevée peut indiquer une étoile de la "deuxième génération" contenant plus de métaux.
    - **Stellar Metallicity Ratio**: Ratio de métallicité de l'étoile hôte
        > Une mesure plus précise de la métallicité, souvent comparée à celle du Soleil (par exemple, [Fe/H]).
    - **Stellar Surface Gravity**: Gravité de surface de l'étoile hôte en cm/s²
        > La force de gravité à la surface de l'étoile, mesurée en centimètres par seconde carrée. Elle affecte la forme et la taille de l'étoile.
    - **Distance**: Distance de l'exoplanète par rapport à la Terre en pc
        > La distance entre la Terre et l'exoplanète, mesurée en parsecs (1 parsec ≈ 3,26 années-lumière).
    - **Gaia Magnitude**: Magnitude de l'étoile hôte
        > La luminosité apparente de l'étoile hôte, mesurée par le satellite Gaia. Plus le nombre est petit, plus l'étoile est lumineuse.
    """)


# Display the Data page
data()
