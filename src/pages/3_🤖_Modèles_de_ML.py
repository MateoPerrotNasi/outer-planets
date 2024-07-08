import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score, confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Chargement des données
data_path = './data/all_exoplanets_2021.csv'
data = pd.read_csv(data_path)

# Configuration de la page Streamlit
st.set_page_config(page_title="Outer Planets", page_icon="🪐", layout="wide")

# Sidebar avec logo
st.sidebar.image("./OP-logo-2.png", use_column_width=True)

# Titre de la section
st.title("🤖 Modèles de ML")

# Sélection du modèle
st.header("Sélection du Modèle")
model_options = ['Régression Linéaire', 'Arbres de Décision', 'Forêt Aléatoire', 'SVM', 'Réseaux Neuronaux']
selected_model = st.selectbox("Choisissez un modèle de machine learning :", model_options)

# Préparation des Données
st.header("Préparation des Données")
st.write("""
Sélectionnez les caractéristiques et la variable cible pour entraîner le modèle. 
Les étapes de séparation et de prétraitement des données sont également incluses.
""")

# Sélection des caractéristiques et de la variable cible
features = st.multiselect("Sélectionnez les caractéristiques :", options=data.columns.tolist(), default=['Orbital Period Days', 'Mass', 'Equilibrium Temperature'])
target = st.selectbox("Sélectionnez la variable cible :", options=data.columns.tolist(), index=data.columns.tolist().index('Stellar Radius'))

# Combinaison des caractéristiques et de la variable cible pour le nettoyage
combined_data = data[features + [target]].dropna()

# Séparation des données en ensembles d'entraînement et de test
X = combined_data[features]
y = combined_data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement et Évaluation du Modèle
st.header("Entraînement et Évaluation du Modèle")
st.write("""
Voici les extraits de code pour l'entraînement du modèle et les résultats obtenus.
Des métriques telles que la précision, le RMSE, la matrice de confusion et la courbe ROC sont affichées.
""")

def train_and_evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
    test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
    train_r2 = r2_score(y_train, y_pred_train)
    test_r2 = r2_score(y_test, y_pred_test)

    return {
        'train_rmse': train_rmse,
        'test_rmse': test_rmse,
        'train_r2': train_r2,
        'test_r2': test_r2,
        'y_pred_test': y_pred_test,
    }

# Sélection et entraînement du modèle
if selected_model == 'Régression Linéaire':
    model = LinearRegression()
elif selected_model == 'Arbres de Décision':
    model = DecisionTreeRegressor()
elif selected_model == 'Forêt Aléatoire':
    model = RandomForestRegressor()
elif selected_model == 'SVM':
    model = SVR()
elif selected_model == 'Réseaux Neuronaux':
    model = MLPRegressor(max_iter=1000)

# Entraînement et évaluation
results = train_and_evaluate_model(model, X_train, X_test, y_train, y_test)

# Affichage des résultats
st.write(f"### Résultats pour {selected_model}")
st.write(f"RMSE d'entraînement : {results['train_rmse']:.2f}")
st.write(f"RMSE de test : {results['test_rmse']:.2f}")
st.write(f"R2 d'entraînement : {results['train_r2']:.2f}")
st.write(f"R2 de test : {results['test_r2']:.2f}")

# Visualisation des prédictions vs valeurs réelles
st.write("#### Prédictions vs Valeurs Réelles")
fig, ax = plt.subplots()
ax.scatter(y_test, results['y_pred_test'])
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
ax.set_xlabel('Valeurs Réelles')
ax.set_ylabel('Prédictions')
ax.set_title('Prédictions vs Valeurs Réelles')
st.pyplot(fig)

# Ajustement des Hyperparamètres
st.header("Ajustement des Hyperparamètres")
st.write("""
Ajustez les hyperparamètres du modèle et observez leur impact sur les performances.
""")

if selected_model == 'Arbres de Décision':
    max_depth = st.slider("Profondeur maximale de l'arbre :", min_value=1, max_value=20, value=5)
    model = DecisionTreeRegressor(max_depth=max_depth)
elif selected_model == 'Forêt Aléatoire':
    n_estimators = st.slider("Nombre d'arbres dans la forêt :", min_value=10, max_value=200, value=100, step=10)
    model = RandomForestRegressor(n_estimators=n_estimators)
elif selected_model == 'SVM':
    C = st.slider("Paramètre de régularisation C :", min_value=0.01, max_value=10.0, value=1.0)
    model = SVR(C=C)
elif selected_model == 'Réseaux Neuronaux':
    hidden_layer_sizes = st.slider("Taille des couches cachées :", min_value=10, max_value=100, value=50, step=10)
    model = MLPRegressor(hidden_layer_sizes=(hidden_layer_sizes,), max_iter=1000)

# Réentraîner le modèle avec les nouveaux hyperparamètres
results = train_and_evaluate_model(model, X_train, X_test, y_train, y_test)

# Affichage des résultats après ajustement des hyperparamètres
st.write(f"### Résultats ajustés pour {selected_model}")
st.write(f"RMSE d'entraînement : {results['train_rmse']:.2f}")
st.write(f"RMSE de test : {results['test_rmse']:.2f}")
st.write(f"R2 d'entraînement : {results['train_r2']:.2f}")
st.write(f"R2 de test : {results['test_r2']:.2f}")

# Visualisation des prédictions vs valeurs réelles après ajustement des hyperparamètres
st.write("#### Prédictions vs Valeurs Réelles (Ajustement des Hyperparamètres)")
fig, ax = plt.subplots()
ax.scatter(y_test, results['y_pred_test'])
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
ax.set_xlabel('Valeurs Réelles')
ax.set_ylabel('Prédictions')
ax.set_title('Prédictions vs Valeurs Réelles (Ajustement des Hyperparamètres)')
st.pyplot(fig)

st.write("---")
st.write("Projet réalisé par PERROT--NASI Matéo et TOMATIS Margot. Pour plus d'informations, vous pouvez nous retrouver sur nos github.")
