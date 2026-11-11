
"""Contrôle de data/prepared/ : lignes, cible 0/1, colonne id retirée."""

import pandas as pd

train = pd.read_csv("data/prepared/train.csv")
test = pd.read_csv("data/prepared/test.csv")

malins = train["diagnosis"].sum()

print(
    f"train : {len(train)} lignes | "
    f"test : {len(test)} lignes | "
    f"colonnes : {train.shape[1]} | "
    f"malins (train) : {malins}"
)

ok = (
    set(train["diagnosis"]) == {0, 1}
    and "id" not in train.columns
)

print(
    "OK : cible 0/1, id retiré."
    if ok
    else "ERREUR : relance dvc repro."
)
