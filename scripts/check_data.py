
"""Contrôle du CSV : taille, cible, valeurs manquantes, empreinte MD5."""
import hashlib
from pathlib import Path
import pandas as pd

CSV = "data/breast_cancer.csv"
REF = "f4aecff5892354dc4c7879d8ee2b3c09"

df = pd.read_csv(CSV)
md5 = hashlib.md5(Path(CSV).read_bytes()).hexdigest()
n = df["diagnosis"].value_counts()

print(
    f"lignes : {len(df)} | colonnes : {df.shape[1]} | "
    f"B={n['B']} M={n['M']}"
)
print(f"manquantes : {df.isna().sum().sum()} | MD5 : {md5}")

print(
    "OK : CSV conforme."
    if md5 == REF
    else "ATTENTION : CSV modifié !"
)
