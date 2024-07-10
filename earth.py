import pandas as pd

# Exemple de dataframe existant (vous avez déjà chargé vos données depuis un fichier CSV)
data = pd.read_csv('data/all_exoplanets_2021.csv')

# Création des données pour les planètes du système solaire
solar_system_data = [
    {'No.': 1, 'Planet Name': 'Mercury', 'Planet Host': 'Sun', 'Num Stars': 1, 'Num Planets': 8,
     'Discovery Method': 'Transit', 'Discovery Year': 1543, 'Discovery Facility': 'Observatoire Copernic',
     'Orbital Period Days': 88, 'Orbit Semi-Major Axis': 0.39, 'Mass': 0.055, 'Eccentricity': 0.205,
     'Insolation Flux': 9126, 'Equilibrium Temperature': 340, 'Spectral Type': 'G2V',
     'Stellar Effective Temperature': 5778, 'Stellar Radius': 1, 'Stellar Mass': 1, 'Stellar Metallicity': 0.0122,
     'Stellar Metallicity Ratio': 1, 'Stellar Surface Gravity': 274, 'Distance': 0.39, 'Gaia Magnitude': -26.74},
    {'No.': 2, 'Planet Name': 'Venus', 'Planet Host': 'Sun', 'Num Stars': 1, 'Num Planets': 8,
     'Discovery Method': 'Transit', 'Discovery Year': 1543, 'Discovery Facility': 'Observatoire Copernic',
     'Orbital Period Days': 225, 'Orbit Semi-Major Axis': 0.72, 'Mass': 0.815, 'Eccentricity': 0.007,
     'Insolation Flux': 2611, 'Equilibrium Temperature': 735, 'Spectral Type': 'G2V',
     'Stellar Effective Temperature': 5778, 'Stellar Radius': 1, 'Stellar Mass': 1, 'Stellar Metallicity': 0.0122,
     'Stellar Metallicity Ratio': 1, 'Stellar Surface Gravity': 274, 'Distance': 0.72, 'Gaia Magnitude': -26.74},
    {'No.': 3, 'Planet Name': 'Earth', 'Planet Host': 'Sun', 'Num Stars': 1, 'Num Planets': 8,
     'Discovery Method': 'Transit', 'Discovery Year': 1543, 'Discovery Facility': 'Observatoire Copernic',
     'Orbital Period Days': 365.25, 'Orbit Semi-Major Axis': 1, 'Mass': 1, 'Eccentricity': 0.0167,
     'Insolation Flux': 1361, 'Equilibrium Temperature': 255, 'Spectral Type': 'G2V',
     'Stellar Effective Temperature': 5778, 'Stellar Radius': 1, 'Stellar Mass': 1, 'Stellar Metallicity': 0.0122,
     'Stellar Metallicity Ratio': 1, 'Stellar Surface Gravity': 274, 'Distance': 1, 'Gaia Magnitude': -26.74},
    {'No.': 4, 'Planet Name': 'Mars', 'Planet Host': 'Sun', 'Num Stars': 1, 'Num Planets': 8,
     'Discovery Method': 'Transit', 'Discovery Year': 1543, 'Discovery Facility': 'Observatoire Copernic',
     'Orbital Period Days': 687, 'Orbit Semi-Major Axis': 1.52, 'Mass': 0.107, 'Eccentricity': 0.093,
     'Insolation Flux': 589, 'Equilibrium Temperature': 210, 'Spectral Type': 'G2V',
     'Stellar Effective Temperature': 5778, 'Stellar Radius': 1, 'Stellar Mass': 1, 'Stellar Metallicity': 0.0122,
     'Stellar Metallicity Ratio': 1, 'Stellar Surface Gravity': 274, 'Distance': 1.52, 'Gaia Magnitude': -26.74},
    {'No.': 5, 'Planet Name': 'Jupiter', 'Planet Host': 'Sun', 'Num Stars': 1, 'Num Planets': 8,
     'Discovery Method': 'Transit', 'Discovery Year': 1543, 'Discovery Facility': 'Observatoire Copernic',
     'Orbital Period Days': 4333, 'Orbit Semi-Major Axis': 5.2, 'Mass': 317.8, 'Eccentricity': 0.049,
     'Insolation Flux': 50, 'Equilibrium Temperature': 124, 'Spectral Type': 'G2V',
     'Stellar Effective Temperature': 5778, 'Stellar Radius': 1, 'Stellar Mass': 1, 'Stellar Metallicity': 0.0122,
     'Stellar Metallicity Ratio': 1, 'Stellar Surface Gravity': 274, 'Distance': 5.2, 'Gaia Magnitude': -26.74},
    {'No.': 6, 'Planet Name': 'Saturn', 'Planet Host': 'Sun', 'Num Stars': 1, 'Num Planets': 8,
     'Discovery Method': 'Transit', 'Discovery Year': 1543, 'Discovery Facility': 'Observatoire Copernic',
     'Orbital Period Days': 10759, 'Orbit Semi-Major Axis': 9.58, 'Mass': 95.2, 'Eccentricity': 0.056,
     'Insolation Flux': 15, 'Equilibrium Temperature': 78, 'Spectral Type': 'G2V',
     'Stellar Effective Temperature': 5778, 'Stellar Radius': 1, 'Stellar Mass': 1, 'Stellar Metallicity': 0.0122,
     'Stellar Metallicity Ratio': 1, 'Stellar Surface Gravity': 274, 'Distance': 9.58, 'Gaia Magnitude': -26.74},
    {'No.': 7, 'Planet Name': 'Uranus', 'Planet Host': 'Sun', 'Num Stars': 1, 'Num Planets': 8,
     'Discovery Method': 'Transit', 'Discovery Year': 1543, 'Discovery Facility': 'Observatoire Copernic',
     'Orbital Period Days': 30688, 'Orbit Semi-Major Axis': 19.22, 'Mass': 14.6, 'Eccentricity': 0.046,
     'Insolation Flux': 4, 'Equilibrium Temperature': 59, 'Spectral Type': 'G2V',
     'Stellar Effective Temperature': 5778, 'Stellar Radius': 1, 'Stellar Mass': 1, 'Stellar Metallicity': 0.0122,
     'Stellar Metallicity Ratio': 1, 'Stellar Surface Gravity': 274, 'Distance': 19.22, 'Gaia Magnitude': -26.74},
    {'No.': 8, 'Planet Name': 'Neptune', 'Planet Host': 'Sun', 'Num Stars': 1, 'Num Planets': 8,
     'Discovery Method': 'Transit', 'Discovery Year': 1543, 'Discovery Facility': 'Observatoire Copernic',
     'Orbital Period Days': 60182, 'Orbit Semi-Major Axis': 30.05, 'Mass': 17.2, 'Eccentricity': 0.01,
     'Insolation Flux': 1.5, 'Equilibrium Temperature': 48, 'Spectral Type': 'G2V',
     'Stellar Effective Temperature': 5778, 'Stellar Radius': 1, 'Stellar Mass': 1, 'Stellar Metallicity': 0.0122,
     'Stellar Metallicity Ratio': 1, 'Stellar Surface Gravity': 274, 'Distance': 30.05, 'Gaia Magnitude': -26.74}
]

# Conversion de la liste en DataFrame
solar_system_df = pd.DataFrame(solar_system_data)

# Ajout des planètes du système solaire au dataframe existant
data = pd.concat([data, solar_system_df], ignore_index=True)

# Sauvegarde du nouveau dataframe avec les planètes du système solaire
data.to_csv('./data/all_exoplanets_with_solar_system.csv', index=False)
