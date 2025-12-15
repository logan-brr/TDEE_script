import pytest

from tdee import calcul_bmr, calcul_tdee, ajuster_objectif

def test_calcul_bmrH():
    bmr = calcul_bmr(sexe='H', poids=70, taille=175, age=25)
    assert round(bmr) == 1674  

def test_calcul_bmrF():
    bmr = calcul_bmr(sexe='F', poids=70, taille=175, age=25)
    assert round(bmr) == 1508 

def test_calcul_tdee():
    bmr = 1674  
    activity_factor = 1.55  
    tdee = calcul_tdee(bmr, activity_factor)
    assert round(tdee) == 2595

def test_ajuster_objectif():
    tdee = 2595  
    objectif_factor = 0.85  
    adjusted_tdee = ajuster_objectif(tdee, objectif_factor)
    assert round(adjusted_tdee) == 2206