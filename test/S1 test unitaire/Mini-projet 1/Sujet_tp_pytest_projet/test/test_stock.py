from application.stock import Stock
import pytest

stk = Stock()
stk.ajouter_produit("livre01", 10)

def test_ajouter_produit():    
    with pytest.raises(ValueError):
        stk.ajouter_produit("livre0",-1)
    assert stk.quantite_disponible("livre01") == 10

def test_retirer_produit():
    with pytest.raises(ValueError):
        stk.retirer_produit("livre01", 20)
    stk.retirer_produit("livre01", 1)
    assert stk.quantite_disponible("livre01") == 9

def test_est_disponible():
    assert stk.est_disponible("livre01", 7) == True
    assert stk.est_disponible("livre01", 10) == False