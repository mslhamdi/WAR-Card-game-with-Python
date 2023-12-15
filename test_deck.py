from Deck import deck
from card import Carte

def access_last_carte():
    carte = Carte(2,Carte.PIQUE)
    deeck = deck()
    deeck.ajoute(carte)
    carte_found = deeck.voir1() 
    return carte_found


def test_ajoute():
    carte = Carte(2,Carte.PIQUE)
    deeck = deck()
    deeck.ajoute(carte)
    assert carte in deeck.D,"erreur test_spade"

def test_nombre():
    deeck = deck()
    for i in range(1,14):
        deeck.ajoute(carte=Carte(i,Carte.PIQUE))
    assert deeck.nombre()==13,f"Erreur test_nombre. Le nombre de carte est de {deeck.nombre()} au lieu de 13 "

def test_supprime():
    deeck=deck()
    carte1 =Carte(1,Carte.PIQUE)
    deeck.ajoute(carte1)
    carte2 =Carte(2,Carte.PIQUE)
    deeck.ajoute(carte2)
    deeck.supprime()
    assert deeck.D==[carte2],"Erreur test_supprime"

def test_voir():
    carte1=Carte(1,Carte.PIQUE)
    carte2=Carte(2,Carte.TREFLE)
    deeck=deck()
    deeck.ajoute(carte1)
    deeck.ajoute(carte2)
    assert deeck.voir()==carte1,"Erreur test_voir"



def tests():
    test_ajoute()
    test_nombre()
    test_supprime()
    test_voir()
    print("All tests passed !")



tests()