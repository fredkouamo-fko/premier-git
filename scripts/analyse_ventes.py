"""Analyse des ventes 2024 - projet data equipe. TEST"""
import csv

def charger_ventes(chemin):
    with open(chemin, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter=";"))

def ca_total(ventes):
    return sum(float(v["montant"]) for v in ventes)

#Analyse des ventes résumée 
if __name__ == "__main__":
    print(f"Nombre de ventes : {len(ventes)}")
    print(f"Chiffre d'affaires total : {ca_total(ventes):.2f} EUR")
