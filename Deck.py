class deck:
    def __init__(self):
        self.D=[]
   
    def ajoute(self,carte):
        self.D=[carte]+self.D

    def supprime(self):
#dans cette fonction on a utilise l'equivalent de return self.D.pop() ,car en fait en utilisant
# en utilisant pop() dans le main les listes se remplissaient par des 'None' ...
        a=self.D[-1]
        self.D=self.D[:-1]
        return a


    def nombre(self):
        return len(self.D)

    def voir(self):
        if len(self.D)!=0:
            return self.D[-1]
        else :
            return None
#on a fait les conditions car ca donnait une erreur dans l'execution d'une partie du pogramme main ...

    def pile(self):
        return self.D

    def remove(self,s):
        if s in self.D:
            self.D.remove(s)
        else:
            pass
#on a fait les conditions car ca donnait une erreur dans l'execution d'une partie du pogramme main ...
    
    def image(self):
        return self.D[-1]

    def ajoute_liste(self,L):
        self.D+=L

    def ajoute_liste_debut(self,L):
        self.D=L+self.D

    def clear(self):
        self.D=[]
