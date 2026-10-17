"""
Module stock.py
----------------
Gestion du stock de livres de la librairie.
Fourni par le développeur.
"""


class Stock:
    def __init__(self):
        self.produits = {}

    def ajouter_produit(self, reference, quantite):
        if quantite < 0:
            raise ValueError("La quantité ne peut pas être négative")
        self.produits[reference] = self.produits.get(reference, 0) + quantite

    def quantite_disponible(self, reference):
        return self.produits.get(reference, 0)

    def retirer_produit(self, reference, quantite):
        disponible = self.quantite_disponible(reference)
        if quantite > disponible:
            raise ValueError(f"Stock insuffisant pour {reference}")
        self.produits[reference] = disponible - quantite

    def est_disponible(self, reference, quantite=1):
        return self.quantite_disponible(reference) >= quantite
