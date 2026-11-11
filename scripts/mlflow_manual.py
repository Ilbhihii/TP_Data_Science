import mlflow
import mlflow.sklearn

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("MLflow Quickstart")

X, y = datasets.load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

params = {
    "solver": "lbfgs",
    "max_iter": 1000,
    "random_state": 8888,
}

with mlflow.start_run(run_name="Iris-Manuel"):
    mlflow.log_params(params)

    lr = LogisticRegression(**params)
    lr.fit(X_train, y_train)

    model_info = mlflow.sklearn.log_model(
        sk_model=lr,
        name="iris_model"
    )

    y_pred = lr.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    mlflow.log_metric("accuracy", accuracy)

    mlflow.set_tag(
        "Training Info",
        "Basic LR model for iris data"
    )

    print("Expérience manuelle terminée !")
    print("Accuracy sur le test :", accuracy)
    print("Modèle enregistré :", model_info.model_uri)