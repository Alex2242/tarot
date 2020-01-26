from context import Joueur

def test_init():
    j = Joueur("nom", 1, 1)
    assert(j.getNumero() == 1)
    assert(j.getType() == 1)

def test_empty():
    j = Joueur("nom", 1, 1)
    assert(j.getCarte() == 23)

def test_change_name():
    j = Joueur("nom", 1, 1)
    j.setNom("nom2")
    assert(j.nom == "nom2")