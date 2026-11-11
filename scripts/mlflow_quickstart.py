import mlflow
import mlflow.sklearn

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Étape 1 : Connexion au serveur MLflow
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("MLflow Quickstart")

# Étape 2 : Chargement des données Iris
X, y = datasets.load_iris(return_X_y=True)

# Séparation des données
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Hyperparamètres
params = {
    "solver": "lbfgs",
    "max_iter": 1000,
    "random_state": 8888,
}

print("Données d'entraînement :", len(X_train))
print("Données de test :", len(X_test))

# Étape 3 : Activer MLflow Autologging
mlflow.sklearn.autolog()

# Entraîner le modèle
lr = LogisticRegression(**params)
lr.fit(X_train, y_train)

print("Entraînement terminé !")
print("Accuracy sur le test :", lr.score(X_test, y_test))