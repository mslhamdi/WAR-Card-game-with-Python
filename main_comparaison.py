from appJar import gui

from card import Carte
from card import comparaison

from Deck import deck
import random

# REMARQUE: dans ce programme comme c ecrite dans l'ennonce, si on a par exemple le as avec 5, ca va
#affiche as<5



D1=deck()
D2=deck()

app = gui()


def fct_comparaison():
    if D1.nombre()==0 or D2.nombre()==0:
        app.setLabel('comparaison','Comparaison impossible')
    else:
        c1=comparaison(D1.pile()[0])
        c2=comparaison(D2.pile()[0])
        if c1.valeur()>10 or c2.valeur()>10:
            app.setLabel('comparaison','<>')
        elif c1==c2:
            app.setLabel('comparaison','=')
        elif c1<c2:
            app.setLabel('comparaison','<')
        elif c1>c2:
            app.setLabel('comparaison','>')
    
    
app.addLabelOptionBox("couleur_1", ["\u2660", "\u2665", "\u2666", "\u2663"], 0, 0)
app.addLabelOptionBox("valeur_1", [str(i) for i in range(1, 14)], 1, 0)


def on_click_1():
    couleur = app.getOptionBox("couleur_1")
    valeur = app.getOptionBox("valeur_1")
    app.setLabel('comparaison','')
    
    if couleur == "\u2660":
        app.setImage("Carte_image_deck_1", Carte(int(valeur), Carte.PIQUE).image())
        D1.ajoute(Carte(int(valeur), Carte.PIQUE).image())
    elif couleur == "\u2665":
        app.setImage("Carte_image_deck_1", Carte(int(valeur), Carte.COEUR).image())
        D1.ajoute(Carte(int(valeur), Carte.COEUR).image())
    elif couleur == "\u2666":
        app.setImage("Carte_image_deck_1", Carte(int(valeur), Carte.CARREAU).image())
        D1.ajoute(Carte(int(valeur), Carte.CARREAU).image())
    elif couleur == "\u2663":
        app.setImage("Carte_image_deck_1", Carte(int(valeur), Carte.TREFLE).image())
        D1.ajoute(Carte(int(valeur), Carte.TREFLE).image())

    app.setLabel('nombre de cartes du Deck 1: ',str(D1.nombre()))
    app.setLabel("message d'erreur",'')
        
def passage():
    try:
        app.setLabel('comparaison','')
        s=random.choice(D1.pile())
        app.setImage("Carte_image_deck_2", s)
        D2.ajoute(s)
        app.setLabel('nombre de cartes du Deck 2: ',str(D2.nombre()))
        D1.remove(s)
        app.setLabel('nombre de cartes du Deck 1: ',str(D1.nombre()))
        if D1.nombre()==0:
            app.setImage("Carte_image_deck_1","resources/empty.gif")
            app.setLabel("message d'erreur",'Le Deck est Vide')
        else:   
            app.setImage("Carte_image_deck_1",D1.voir())
        app.setLabel("message d'erreur",'')
    except:
        app.setLabel('comparaison','')

        if D1.nombre()==0 and D2.nombre()==0:
            app.setLabel("message d'erreur","Le Deck est Vide")

        if D1.nombre()==0:
            app.setLabel("message d'erreur","Le Deck est Vide")
        else:
            pass


app.setsize(100,300)

app.addLabel("comparaison",'',6,1)

app.addButton("affiche carte_1", on_click_1, 2, 0)
app.addButton("passage",passage,2,1)
app.addButton('comparaison',fct_comparaison,6,2)

app.addLabel("message d'erreur","",5,0)

app.addLabel('nombre de cartes du Deck 1: ',str(D1.nombre()),4,0)
app.addLabel('nombre de cartes du Deck 2: ',str(D2.nombre()),4,1)

app.addImage("Carte_image_deck_1", "resources/empty.gif", 3, 0)
app.addImage('Carte_image_deck_2',"resources/empty.gif", 3, 1)

app.go()

