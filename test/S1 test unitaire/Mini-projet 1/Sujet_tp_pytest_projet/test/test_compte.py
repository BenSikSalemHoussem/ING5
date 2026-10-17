from application.compte import Compte
import pytest


client = Compte("Houssem", 1000)

def test_creata_account():
    assert client.titulaire == "Houssem"
    assert client.solde == 1000
    assert client.historique == []

@pytest.mark.parametrize("titulaire", [None, ""])
def test_create_account_without_titulaire(titulaire):
    with pytest.raises(ValueError):
        Compte(titulaire)

def test_depose():
    client.deposer(500)
    assert client.solde == 1500
    with pytest.raises(ValueError):
        client.deposer(-500)

def test_retiser():
    client.retirer(500)
    assert client.solde == 1000
    with pytest.raises(ValueError):
        client.retirer(-500)
    with pytest.raises(ValueError):
        client.retirer(1500)

def test_nombre_operations():
    client.nombre_operations()
    assert len(client.historique) == 2
    assert client.historique == [("depot", 500),("retrait", 500)]