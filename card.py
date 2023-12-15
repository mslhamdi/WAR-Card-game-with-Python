class Carte:
    PIQUE = "spade"
    COEUR = "heart"
    CARREAU = "diamond"
    TREFLE = "club"
    

    def __init__(self, valeur, couleur):
        self._valeur = valeur
        self._couleur = couleur

    def image(self):
        return "resources/Playing_card_" + self._couleur + "_" + str(self._valeur) + ".gif"

class comparaison:
    def __init__(self,lien_d_image):
        self.ch=''
        self.nombres='0123456789'
        for i in lien_d_image:
            if i in self.nombres:
                self.ch+=str(i)
            #else:
                #pass
        self.valeurr=int(self.ch)
#le but de cette initialisation c d'avoir la valeur de la carte a partir du 'lien' (dans le fichier ressource) de
#de la carte car en effet les piles D1 et D2 du main sont rempliees par des liens

    def valeur(self):
        return self.valeurr

    def __eq__(self,other):
        return self.valeurr==other.valeurr

            
    def __gt__(self,other):
        return self.valeurr>other.valeurr

    
    def __lt__(self,other):
        return self.valeurr<other.valeurr


