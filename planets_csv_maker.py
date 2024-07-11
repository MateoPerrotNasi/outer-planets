import csv
import random

# Define columns
columns = [
    "No.", "Planet Name", "Planet Host", "Num Stars", "Num Planets", "Discovery Method",
    "Discovery Year", "Discovery Facility", "Orbital Period Days", "Orbit Semi-Major Axis",
    "Mass", "Eccentricity", "Insolation Flux", "Equilibrium Temperature", "Spectral Type",
    "Stellar Effective Temperature", "Stellar Radius", "Stellar Mass", "Stellar Metallicity",
    "Stellar Metallicity Ratio", "Stellar Surface Gravity", "Distance", "Gaia Magnitude"
]

# Generate fake data
planet_names = ["Aegon", "Boreas", "Cynosure", "Dione", "Erebus", "Faunus", "Gaia", "Hestia", "Io", "Juno",
                "Kronos", "Luna", "Morpheus", "Nereid", "Orion", "Phobos", "Quirinus", "Rhea", "Selene", "Tethys",
                "Umbriel", "Vesta", "Weyland", "Xanthus", "Ymir", "Zephyr", "Hyperion", "Lyra", "Marsyas", "Nysa",
                "Oberon", "Pan", "Quasar", "Rhadamanthys", "Sirius", "Titan", "Ulysses", "Vulcan", "Wolf", "Xena",
                "Ymir", "Zeus", "Achilles", "Bragi", "Calypso", "Deimos", "Elara", "Freya", "Ganymede", "Helios"]

discovery_methods = ["Transit", "Radial Velocity", "Direct Imaging", "Microlensing", "Astrometry", "Timing"]
discovery_facilities = ["Kepler", "Hubble", "Spitzer", "VLT", "ALMA", "JWST"]
spectral_types = ["O", "B", "A", "F", "G", "K", "M"]


def random_float(min_value, max_value, precision=2):
    return round(random.uniform(min_value, max_value), precision)


# Generate rows
rows = []
for i in range(1, 51):
    row = [
        i,
        random.choice(planet_names),
        f"Host_{i}",
        random.randint(1, 5),
        random.randint(1, 10),
        random.choice(discovery_methods),
        random.randint(1990, 2023),
        random.choice(discovery_facilities),
        random_float(1, 3650),
        random_float(0.1, 50),
        random_float(0.1, 50),
        random_float(0, 1),
        random_float(0.1, 300),
        random.randint(50, 2000),
        random.choice(spectral_types),
        random.randint(2000, 50000),
        random_float(0.1, 10),
        random_float(0.1, 10),
        random_float(-2.5, 0.5),
        random_float(0.1, 1),
        random_float(2, 5),
        random_float(1, 1000),
        random_float(1, 20)
    ]
    rows.append(row)

# Save to CSV
csv_filename = "/data/test_planets1.csv"
with open(csv_filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(columns)
    csvwriter.writerows(rows)