import sys
import mlflow
import pandas as pd

from sklearn import datasets
from sklearn.model_selection import train_test_split

# Connexion au serveur
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Adresse du modèle enregistrée dans MLflow
model_uri = sys.argv[1]

# Charger le modèle sans le réentraîner
loaded_model = mlflow.pyfunc.load_model(model_uri)

# Reprendre les mêmes données Iris
iris = datasets.load_iris()
X, y = iris.data, iris.target

_, X_test, _, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Réaliser les prédictions
predictions = loaded_model.predict(X_test)

# Afficher les résultats
result = pd.DataFrame(
    X_test,
    columns=iris.feature_names
)
result["actual_class"] = y_test
result["predicted_class"] = predictions

print(result.head(4).to_string(index=False))