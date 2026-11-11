# Projet Data Science

## Données

Jeu : UCI Breast Cancer Wisconsin (Diagnostic), 569 observations.
Cible : `diagnosis` (B=0, M=1), encodée par `src/prepare.py`.

- Déclarer le stockage : `dvc remote add --local -d storage <dossier>`
- Récupérer les données : `dvc pull`
- (ou les retélécharger depuis UCI : `python scripts/get_data.py`)
- Rejouer la préparation : `dvc repro`
- Version de référence : tag `data-bc-v1`