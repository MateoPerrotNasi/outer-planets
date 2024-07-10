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
