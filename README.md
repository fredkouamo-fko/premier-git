# Projet Ventes 2024 — Analyse Data

Projet de démonstration pour la masterclass Git. Il simule un vrai projet Data Analyst versionné en équipe : analyse des ventes 2024 par région et par produit.

## Structure

```
projet_data/
├── data/               jeux de données (échantillon versionné)
│   └── ventes_2024.csv
├── scripts/            scripts d'analyse Python
│   └── analyse_ventes.py
├── sql/                requêtes SQL
│   └── requetes_analyse.sql
├── notebooks/          notebooks d'exploration
├── dashboards/         exports et fichiers de dashboard
├── docs/               documentation et journal du projet
│   └── journal_projet.md
├── config.example.py   modèle de configuration (à copier en config.py)
├── requirements.txt    dépendances Python
├── .gitignore          fichiers exclus du versioning
└── README.md
```

## Mise en route

```bash
# 1. Copier la config et la remplir (config.py est ignoré par Git)
cp config.example.py config.py

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer l'analyse
python scripts/analyse_ventes.py
```

## Note importante

Le fichier `config.py` contient des identifiants sensibles et n'est **jamais** versionné (voir `.gitignore`). On versionne uniquement `config.example.py` comme modèle.

---

Projet réalisé dans le cadre d'une masterclass par Julien Séré, Data Analyst & créateur de contenu data.
