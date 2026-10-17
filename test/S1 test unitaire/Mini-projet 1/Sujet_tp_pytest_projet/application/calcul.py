"""
Module calcul.py
-----------------
Fonctions de calcul utilisées par la librairie en ligne "Le Savoir".
Ce module est fourni par le développeur. Il ne doit PAS être modifié
par l'étudiant-testeur.
"""


def addition(a, b):
    """Retourne la somme de deux nombres."""
    return a + b


def division(a, b):
    """Retourne la division de a par b.

    Lève une ValueError si b vaut 0.
    """
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b


def prix_total(prix_unitaire, quantite):
    """Calcule le prix total d'une ligne de commande.

    Lève une ValueError si le prix ou la quantité est négatif.
    """
    if prix_unitaire < 0 or quantite < 0:
        raise ValueError("Le prix et la quantité doivent être positifs")
    return round(prix_unitaire * quantite, 2)


def appliquer_remise(prix, pourcentage):
    """Applique un pourcentage de remise à un prix.

    Lève une ValueError si le pourcentage n'est pas compris entre 0 et 100.
    """
    if pourcentage < 0 or pourcentage > 100:
        raise ValueError("Pourcentage de remise invalide")
    return round(prix - (prix * pourcentage / 100), 2)


def moyenne(notes):
    """Calcule la moyenne d'une liste de notes.

    Lève une ValueError si la liste est vide.
    """
    if not notes:
        raise ValueError("La liste est vide")
    return sum(notes) / len(notes)
