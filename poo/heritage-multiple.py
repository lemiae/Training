# Heritage multiple : multiple inheritance

class EtreVivant:
    def afficher_infos(self):
        print("Je suis un être vivant")

class Predateur:
    def chasser_manger_proie(self):
        print("miam miam")

class Lion(EtreVivant, Predateur): # Heritage multiple !
    def afficher_infos(self):
        print("Je suis un lion")

class Personne(EtreVivant):
    def afficher_infos(self):
        print("Je suis une personne")

lion = Lion()
lion.afficher_infos()
lion.chasser_manger_proie()

