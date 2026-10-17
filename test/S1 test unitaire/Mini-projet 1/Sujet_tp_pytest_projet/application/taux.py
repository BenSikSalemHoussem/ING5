"""
Module taux.py
---------------
Simule un service externe (ex : taux de TVA fourni par un serveur distant).
Fourni par le développeur. Sert à illustrer monkeypatch/mock, car on ne
peut pas dépendre d'un vrai service externe pendant les tests.
"""

import time


def recuperer_taux_tva():
    """Simule un appel réseau lent vers un service externe de taux de TVA."""
    time.sleep(2)  # simule une latence réseau
    return 20.0  # taux fixe renvoyé "par le serveur"


def calculer_prix_ttc(prix_ht):
    """Calcule le prix TTC à partir du taux de TVA récupéré à distance."""
    taux = recuperer_taux_tva()
    return round(prix_ht * (1 + taux / 100), 2)
