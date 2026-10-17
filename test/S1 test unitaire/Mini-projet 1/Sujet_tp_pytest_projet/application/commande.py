"""
Module commande.py
-------------------
Création d'une commande client : vérifie le stock, calcule le total,
et met à jour le stock. Fourni par le développeur.
"""

from application.calcul import prix_total, appliquer_remise


class Commande:
    def __init__(self, client, stock):
        self.client = client
        self.stock = stock
        self.lignes = []
        self.statut = "en_attente"

    def ajouter_ligne(self, reference, prix_unitaire, quantite):
        if not self.stock.est_disponible(reference, quantite):
            raise ValueError(f"Rupture de stock pour {reference}")
        self.lignes.append(
            {"reference": reference, "prix": prix_unitaire, "quantite": quantite}
        )

    def total(self, remise=0):
        total = sum(prix_total(l["prix"], l["quantite"]) for l in self.lignes)
        if remise:
            total = appliquer_remise(total, remise)
        return round(total, 2)

    def valider(self):
        if not self.lignes:
            raise ValueError("Impossible de valider une commande vide")
        for ligne in self.lignes:
            self.stock.retirer_produit(ligne["reference"], ligne["quantite"])
        self.statut = "validee"
        return self.statut
