from application.calcul import addition, appliquer_remise, division, moyenne, prix_total

def test_addition():
    assert addition(-3,2) == -1



import json
import pytest

with open("data/data_test_calcul.json", "r") as file:
    data = json.load(file)

@pytest.mark.parametrize("case", data["addition"])
def test_addition2(case):
    assert addition(case["a"], case["b"]) == case["result"]



@pytest.mark.parametrize("case", data["division"])
def test_devision(case):
    if  "exception" in case :
        with pytest.raises(ValueError, match="Division par zéro impossible"):
            division(case["a"], case["b"])
    else :
        assert division(case["a"], case["b"]) == case["result"] 



@pytest.mark.parametrize("case", data["prix_total"])
def test_prix_total(case):
    if  "exception" in case :
        with pytest.raises(ValueError):
            prix_total(case["prix_unitaire"], case["quantite"])
    else :
        assert prix_total(case["prix_unitaire"], case["quantite"]) == case["result"] 




@pytest.mark.parametrize("case", data["appliquer_remise"])
def test_appliquer_remise(case):
    if  "exception" in case :
        with pytest.raises(ValueError):
            appliquer_remise(case["prix"], case["pourcentage"])
    else :
        assert appliquer_remise(case["prix"], case["pourcentage"]) == case["result"] 




@pytest.mark.parametrize("case", data["moyenne"])
def test_moyenne(case):
    if  "exception" in case :
        with pytest.raises(ValueError):
            moyenne(case["notes"])
    else :
        assert moyenne(case["notes"]) == case["result"] 