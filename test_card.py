from card import Carte


carte=Carte(1,Carte.PIQUE)
couleur= Carte.PIQUE
valeur= 1
assert carte.image()=="resources/Playing_card_" + couleur + "_" + str(valeur) + ".gif", "Erreur, carte différente de l'as de pique"