"""
Module compte.py
-----------------
Représente le compte fidélité d'un client de la librairie "Le Savoir".
Fourni par le développeur.
"""


class Compte:
    """Compte fidélité d'un client (solde en points ou en euros)."""

    def __init__(self, titulaire, solde=0):
        if not titulaire:
            raise ValueError("Le titulaire est obligatoire")
        self.titulaire = titulaire
        self.solde = solde
        self.historique = []

    def deposer(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        self.solde += montant
        self.historique.append(("depot", montant))

    def retirer(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        if montant > self.solde:
            raise ValueError("Solde insuffisant")
        self.solde -= montant
        self.historique.append(("retrait", montant))

    def nombre_operations(self):
        return len(self.historique)
