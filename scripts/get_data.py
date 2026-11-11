
"""Télécharge le jeu de l'UCI et écrit data/breast_cancer.csv."""
import io
import urllib.request
import zipfile
from pathlib import Path

URL = ("https://archive.ics.uci.edu/static/public/17/"
       "breast+cancer+wisconsin+diagnostic.zip")

MESURES = [
    "radius", "texture", "perimeter", "area", "smoothness",
    "compactness", "concavity", "concave_points", "symmetry",
    "fractal_dimension"
]

COLONNES = ["id", "diagnosis"] + [
    f"{m}_{s}"
    for s in ("mean", "se", "worst")
    for m in MESURES
]

uci = zipfile.ZipFile(
    io.BytesIO(urllib.request.urlopen(URL).read())
)

lignes = uci.read("wdbc.data").decode().splitlines()

Path("data").mkdir(exist_ok=True)
Path("data/breast_cancer.csv").write_text(
    "\n".join([",".join(COLONNES)] + lignes) + "\n",
    newline="\n"
)

print(
    f"data/breast_cancer.csv : "
    f"{len(lignes)} observations téléchargées"
)

