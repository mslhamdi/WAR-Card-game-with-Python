from appJar import gui

from card import Carte
from card import comparaison

from Deck import deck
import random

app = gui()

D1=deck() #le D1 ca va contenir les cartes du joueur 1 (qui est a gauche dans l'interface graphique)
D2=deck() #le D2 ca va contenir les cartes du joueur 2 (qui est a droite dans l'interface graphique)
D3=deck() #le D3 ca va contenir les cartes qu on va ajouter si on a egalite c est a dire lorsqu on va
#proceder a la Bataille, les cartes deployees seront dtockes dans D3 puis seront affectees au gagnant
#au gagnant a la fin de la bataille ..

def distribuer_cartes():
#cette fonction c elle qui va distribuer les cartes aleatoirement, c est a dire donner aleatoirement
#donner aleatoirement 26 cartes a chaque joueur
    color=["\u2660", "\u2665", "\u2666", "\u2663"]
    value=[str(i) for i in range(1, 14)]
    cartes_possibles=deck()
    for i in color:
        for j in value:
            cartes_possibles.ajoute((i,j))
#ici maintenant la liste de cartes_possibles contient tous les tuples des cartes possibles
#sous forme de (couleur,valeur)...
    app.setImage("Carte_image_deck_1", "resources/Aluette_card_deck_-_Grimaud_-_1858-1890_-_Back_side.gif")
    app.setImage("Carte_image_deck_2", "resources/Aluette_card_deck_-_Grimaud_-_1858-1890_-_Back_side.gif")
#on a fait ces set pour ne pas voir l'image de la carte mais voir le dos de la carte...
    while cartes_possibles.nombre()!=26:
        s=random.choice(cartes_possibles.pile())
        affecter_carte(D1,s[0],s[1],1)
#la fonction affecter_carte se trouve ci dessous, elle permet d'affecter une carte a un deck(), dans ce
#cas elle l'affecte a D1 
        cartes_possibles.remove(s)
    while cartes_possibles.nombre()!=0:
        s=random.choice(cartes_possibles.pile())
        affecter_carte(D2,s[0],s[1],2)
        #cartes_possibles.remove(s)
        cartes_possibles.remove(s)


def affecter_carte(joueur,couleur,valeur,i):
#ici on s'est inspire par la fonction on_click definie sur l'exercice...
    app.setImage("Carte_image_deck_1","resources/Aluette_card_deck_-_Grimaud_-_1858-1890_-_Back_side.gif")
    if couleur == "\u2660":

        joueur.ajoute(Carte(int(valeur), Carte.PIQUE).image())
    elif couleur == "\u2665":

        joueur.ajoute(Carte(int(valeur), Carte.COEUR).image())
    elif couleur == "\u2666":

        joueur.ajoute(Carte(int(valeur), Carte.CARREAU).image())
    elif couleur == "\u2663":

        joueur.ajoute(Carte(int(valeur), Carte.TREFLE).image())

    app.setLabel('nombre de cartes du Deck '+str(i)+': ',str(joueur.nombre()))
    app.setLabel("message d'erreur",'')
        
    


def fct_jouer():
#cette fonction explique et contient les regles de jeu

    if D1.nombre()==0 and D2.nombre()==0:
        app.setLabel('comparaison',"Il faut d'abord distribuer les cartes pour pouvoir jouer")
    if D1.nombre()==0 and D2.nombre()!=0 :
        if D3.nombre()==0:
            app.setLabel('comparaison','le joueur 2 est vainqueur')
        else:
            app.setLabel('comparaison','Match Nul')

    if D2.nombre()==0 and D1.nombre()!=0 :
        if D3.nombre()==0:
            app.setLabel('comparaison','le joueur 1 est vainqueur')
        else:
            app.setLabel('comparaison','Match Nul')
#il ya ici trois principales if, les deux dernieres serrent a ne pas avoir une erreur lorsqu on appuie
#sur coup suivant lorsque le jeu est termine

    else:
        c1=comparaison(D1.voir())
        c2=comparaison(D2.voir())
#le but des deux lignes precedents c d'acceder aux valeurs des dernieres cartes de D1 et D2
#c est a dire les cartes du dessus, CAR en fait D1 et D2 contiennent des liens d'images...
        app.setImage("Carte_image_deck_1","resources/Aluette_card_deck_-_Grimaud_-_1858-1890_-_Back_side.gif")
        app.setImage("Carte_image_deck_2","resources/Aluette_card_deck_-_Grimaud_-_1858-1890_-_Back_side.gif")
    
    
    
        if D3.nombre()!=0 and (D3.nombre()/2)%2!=0:
            app.setImage("Carte_image_deck_1_jeu_de_bataille","resources/Aluette_card_deck_-_Grimaud_-_1858-1890_-_Back_side.gif")
            app.setImage("Carte_image_deck_2_jeu_de_bataille","resources/Aluette_card_deck_-_Grimaud_-_1858-1890_-_Back_side.gif")
            #ces deux lignes pour cacher les cartes pendant la bataille ,c est a dire quand on trouve egalite 
#le coup suivant on pose des cartes cachees
            D3.ajoute(D1.supprime()) #c la carte cache
            D3.ajoute(D2.supprime()) #c la carte cache
            if D1.nombre()==0 or D2.nombre()==0:
                app.setLabel('comparaison','Match Nul')
            #cette derniere condition dans le cas par exemple ou le joueur 1 a deux cartes restantes et
#le joueur 2 a 50 cartes restantes. On appuie sur coup suivant c la condition c1==c2 qui va etre execute
#par exemple, donc il va rester une pour joueur 1 et 51 pour 2, et puis dans le coup suivant
#les deux cartes vont etre cache car on est dans la Bataille, donc la derniere carte du joueur 1
#va etre cache et ne vas pas etre compare... D'apres les regles de jeu dans wikipedia, dans ce cas
#on pourra annoocer match nul
            app.setLabel('nombre de cartes du Deck 2: ',str(D2.nombre()))
            app.setLabel('nombre de cartes du Deck 1: ',str(D1.nombre()))
    
        
        elif c1.valeur()==1 and c2.valeur()!=1:
#le cas de as dans D1 avec n'importe quelle carte
            #app.setLabel('comparaison','>')
            app.setImage("Carte_image_deck_1_jeu_de_bataille",D1.image())
            app.setImage("Carte_image_deck_2_jeu_de_bataille",D2.image())
#faut faire set image d'abord et puis modifier D1 et D2
            D1.ajoute_liste_debut(D3.pile())
            D3.clear()
#les deux dernieres lignes: on va ajouter le D3 qui ramasse les cartes dans le cas d'egalite(bataille)
#on va l'ajouter au gagnant dans ce cas c le D1, et puis on doit vider D3 avec clear() pour que la
#memoire ou les cartes qui etait avant ne restent pas stockees au cas ou il ya une deuxieme bataille...
    
            app.setLabel('comparaison','>')
            D1.ajoute(D2.supprime())
            D1.ajoute(D1.supprime())
    
            app.setLabel('nombre de cartes du Deck 2: ',str(D2.nombre()))
            app.setLabel('nombre de cartes du Deck 1: ',str(D1.nombre()))
    
            if D2.nombre()==52:
                app.setLabel('comparaison','le joueur 2 est vainqueur')
                app.setImage("Carte_image_deck_1","resources/empty.gif")
            if D1.nombre()==52:
                app.setLabel('comparaison','le joueur 1 est vainqueur')
                app.setImage("Carte_image_deck_2","resources/empty.gif")
            #ces deux derniers if c pour le cas par exemple ou il reste pour le joueur 1, une carte et pour
#le 2, il lui reste 51 cartes, dans ce cas, j'ai fait ces deux if dans toutes les conditions elif
#pour que quand je vais appuyer sur jouer(qui est coup suivant), l'image du deck 1 va devenir vide
#et ca va s'affcher: le joueur 2 est vainqueur
    
    
        elif c2.valeur()==1 and c1.valeur()!=1:
            #app.setLabel('comparaison','<')
            app.setImage("Carte_image_deck_1_jeu_de_bataille",D1.image())
            app.setImage("Carte_image_deck_2_jeu_de_bataille",D2.image())
            D2.ajoute_liste_debut(D3.pile())
            D3.clear()
            app.setLabel('comparaison','<')
            D2.ajoute(D1.supprime())
            D2.ajoute(D2.supprime())
    
            app.setLabel('nombre de cartes du Deck 2: ',str(D2.nombre()))
            app.setLabel('nombre de cartes du Deck 1: ',str(D1.nombre()))
            if D2.nombre()==52:
                app.setLabel('comparaison','le joueur 2 est vainqueur')
                app.setImage("Carte_image_deck_1","resources/empty.gif")
            if D1.nombre()==52:
                app.setLabel('comparaison','le joueur 1 est vainqueur')
                app.setImage("Carte_image_deck_2","resources/empty.gif")
    
    
        elif c1<c2:
            app.setLabel('comparaison','<')
            app.setImage("Carte_image_deck_1_jeu_de_bataille",D1.image())
            app.setImage("Carte_image_deck_2_jeu_de_bataille",D2.image())
            D2.ajoute_liste_debut(D3.pile())
            D3.clear()
            D2.ajoute(D1.supprime())
            D2.ajoute(D2.supprime())
    
            #app.setLabel('comparaison','<')
            app.setLabel('nombre de cartes du Deck 2: ',str(D2.nombre()))
            app.setLabel('nombre de cartes du Deck 1: ',str(D1.nombre()))
            if D2.nombre()==52:
                app.setLabel('comparaison','le joueur 2 est vainqueur')
                app.setImage("Carte_image_deck_1","resources/empty.gif")
            if D1.nombre()==52:
                app.setLabel('comparaison','le joueur 1 est vainqueur')
                app.setImage("Carte_image_deck_2","resources/empty.gif")
    
    
        elif c1==c2:
# c le cas de la  bataille
            app.setLabel('comparaison',' BATAILLE')
            app.setImage("Carte_image_deck_1_jeu_de_bataille",D1.image())
            app.setImage("Carte_image_deck_2_jeu_de_bataille",D2.image())
            D3.ajoute(D1.supprime())
            D3.ajoute(D2.supprime())
            #les cartes egales vont etre stockes dans D3
# et apres quand on va apuyer sur jouer(qui est coup suivant), ca va automatiquement verifier la premiers 
#condition de la fct_jouer qui est if D3.nombre()!=0 and (D3.nombre()/2)%2!=0:
#et ca la ou se montre l'IMPORTANCE DE L'ORDRE utilise dans cette fonction car je travaille avec
#les elif et non pas les if ...
            app.setLabel('nombre de cartes du Deck 2: ',str(D2.nombre()))
            app.setLabel('nombre de cartes du Deck 1: ',str(D1.nombre()))
            if D2.nombre()==52:
                app.setLabel('comparaison','le joueur 2 est vainqueur')
                app.setImage("Carte_image_deck_1","resources/empty.gif")
            if D1.nombre()==52:
                app.setLabel('comparaison','le joueur 1 est vainqueur')
                app.setImage("Carte_image_deck_2","resources/empty.gif")
    
        
        elif c1>c2:
            app.setLabel('comparaison','>')
            app.setImage("Carte_image_deck_1_jeu_de_bataille",D1.image())
            app.setImage("Carte_image_deck_2_jeu_de_bataille",D2.image())
            D1.ajoute_liste_debut(D3.pile())
            D3.clear()
    
            D1.ajoute(D2.supprime())
            D1.ajoute(D1.supprime())
    
            app.setLabel('comparaison','>')
            app.setLabel('nombre de cartes du Deck 2: ',str(D2.nombre()))
            app.setLabel('nombre de cartes du Deck 1: ',str(D1.nombre()))
            if D2.nombre()==52:
                app.setLabel('comparaison','le joueur 2 est vainqueur')
                app.setImage("Carte_image_deck_1","resources/empty.gif")
            if D1.nombre()==52:
                app.setLabel('comparaison','le joueur 1 est vainqueur')
                app.setImage("Carte_image_deck_2","resources/empty.gif")
    
def affiche_dessus1():
    if D1.nombre()==0:
        app.setLabel("message d'erreur","Le Deck 1 est Vide")
    else:
        app.setImage("Carte_image_deck_1",D1.image())
#ces deux fcts de dessus c juste pour s'assurer que vraiment c la carte du dessus qui va etre joue
#et compare avec l'autre carte...

def affiche_dessus2():
    if D2.nombre()==0:
        app.setLabel("message d'erreur","Le Deck 2 est Vide")
    else:
        app.setImage("Carte_image_deck_2",D2.image())

app.setsize(100,300)

app.addLabel("message d'erreur","",5,0)

app.addLabel("comparaison",'',6,2)


app.addButton('coup suivant',fct_jouer,7,3)
app.addButton('distribution des cartes',distribuer_cartes,1,0)
#app.addTitle('Titre','JEU DE BATAILLE',0,0)

app.addButton('afficher la carte du dessus du deck 1',affiche_dessus1,6,0)
app.addButton('afficher la carte du dessus du deck 2',affiche_dessus2,6,3)


app.addLabel('nombre de cartes du Deck 1: ',str(D1.nombre()),4,0)
app.addLabel('nombre de cartes du Deck 2: ',str(D2.nombre()),4,3)

app.addImage("Carte_image_deck_1", "resources/empty.gif", 3, 0)
app.addImage('Carte_image_deck_2',"resources/empty.gif", 3, 3)

app.addImage("Carte_image_deck_1_jeu_de_bataille", "resources/empty.gif", 3, 1)
app.addImage('Carte_image_deck_2_jeu_de_bataille',"resources/empty.gif", 3, 2)

app.go()

