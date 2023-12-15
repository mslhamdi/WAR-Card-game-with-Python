from appJar import gui

from card import Carte
from Deck import deck
import random

D1=deck()
D2=deck()


app = gui()

app.addLabelOptionBox("couleur_1", ["\u2660", "\u2665", "\u2666", "\u2663"], 0, 0)
app.addLabelOptionBox("valeur_1", [str(i) for i in range(1, 14)], 1, 0)


def on_click_1():
    couleur = app.getOptionBox("couleur_1")
    valeur = app.getOptionBox("valeur_1")
    app.setImage("Carte_image_deck_1","resources/Aluette_card_deck_-_Grimaud_-_1858-1890_-_Back_side.gif")
#c cette derniere ligne qui nous set l'image pour qu on voit que le dos de la carte lors du click 
#sur le bouton
    if couleur == "\u2660":

        D1.ajoute(Carte(int(valeur), Carte.PIQUE).image())
    elif couleur == "\u2665":

        D1.ajoute(Carte(int(valeur), Carte.COEUR).image())
    elif couleur == "\u2666":

        D1.ajoute(Carte(int(valeur), Carte.CARREAU).image())
    elif couleur == "\u2663":

        D1.ajoute(Carte(int(valeur), Carte.TREFLE).image())
    
    if D1.nombre()==0:
        app.setImage("Carte_image_deck_1", "resources/empty.gif")


    app.setLabel('nombre de cartes du Deck 1: ',str(D1.nombre()))
    app.setLabel("message d'erreur",'')
        
def passage():
    try:
        s=random.choice(D1.pile())

        D2.ajoute(s)
        app.setLabel('nombre de cartes du Deck 2: ',str(D2.nombre()))
        app.setImage("Carte_image_deck_2","resources/Aluette_card_deck_-_Grimaud_-_1858-1890_-_Back_side.gif")
        #c cette derniere ligne qui nous montre le dos de la carte lors de l'appui sur passage
        D1.remove(s)
        app.setLabel('nombre de cartes du Deck 1: ',str(D1.nombre()))
        app.setLabel("message d'erreur",'')
        if D1.nombre()==0:
            app.setImage("Carte_image_deck_1","resources/empty.gif")
            
        else:   

            app.setImage("Carte_image_deck_1","resources/Aluette_card_deck_-_Grimaud_-_1858-1890_-_Back_side.gif")
            app.setLabel("message d'erreur",'')
    except:
        
        if D1.nombre()==0 and D2.nombre()==0:
            app.setLabel("message d'erreur","Le Deck 1 est Vide")
        
        elif D1.nombre()==0 and D2.nombre()!=0:
            app.setLabel("message d'erreur","Le Deck 1 est Vide")

        elif D1.nombre()==0:
            app.setLabel("message d'erreur","Le Deck 1 est Vide")
        else:
            pass
#cas dyal d1 3amar puis passage a d2 puis d1 vide puis passage ca saffiche pas deck est vide
def affiche_dessus1():
    if D1.nombre()==0:
        app.setLabel("message d'erreur","Le Deck 1 est Vide")
    else:
        app.setImage("Carte_image_deck_1",D1.image())



def affiche_dessus2():
    if D2.nombre()==0:
        app.setLabel("message d'erreur","Le Deck 2 est Vide")
    else:
        app.setImage("Carte_image_deck_2",D2.image())


app.setsize(100,300)
app.addLabel("message d'erreur","",5,0)

app.addButton("affiche carte_1", on_click_1, 2, 0)
app.addButton("passage",passage,2,1)
app.addButton('afficher la carte du dessus du deck 1',affiche_dessus1,6,0)
app.addButton('afficher la carte du dessus du deck 2',affiche_dessus2,6,1)


app.addLabel('nombre de cartes du Deck 1: ',str(D1.nombre()),4,0)
app.addLabel('nombre de cartes du Deck 2: ',str(D2.nombre()),4,1)

app.addImage("Carte_image_deck_1", "resources/empty.gif", 3, 0)
app.addImage('Carte_image_deck_2',"resources/empty.gif", 3, 1)

app.go()