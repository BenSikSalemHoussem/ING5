"""
Module utilisateur.py
----------------------
Gestion et validation des utilisateurs (clients) de la librairie.
Fourni par le développeur.
"""

import re

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"


class Utilisateur:
    def __init__(self, nom, email, age):
        self.nom = nom
        self.email = email
        self.age = age

    def est_email_valide(self):
        return re.match(EMAIL_REGEX, self.email) is not None

    def est_majeur(self):
        return self.age >= 18

    def inscrire(self):
        """Valide l'inscription d'un utilisateur.

        Lève une ValueError si le nom est vide, l'email invalide,
        ou si l'utilisateur est mineur.
        """
        if not self.nom or not self.nom.strip():
            raise ValueError("Le nom est obligatoire")
        if not self.est_email_valide():
            raise ValueError("Email invalide")
        if not self.est_majeur():
            raise ValueError("L'utilisateur doit être majeur")
        return True
