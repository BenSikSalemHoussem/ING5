"""
Module api.py
--------------
Simule un appel à une API externe (ex : service de recherche de livres
par ISBN chez un fournisseur). Fourni par le développeur.
Sert à illustrer les tests d'API avec des mocks (sans appel réseau réel).
"""

import requests


def rechercher_livre(isbn):
    """Interroge une API externe pour récupérer les informations d'un livre.

    En conditions réelles, ceci ferait un appel HTTP. Dans le TP, cette
    fonction est simulée (mockée) dans les tests afin de ne jamais
    dépendre d'un vrai service réseau.
    """
    reponse = requests.get(f"https://api-livres.example.com/isbn/{isbn}", timeout=5)
    if reponse.status_code != 200:
        raise ValueError("Livre introuvable")
    return reponse.json()
