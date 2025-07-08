# __str__ et __repr__

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        
        
    def AfficherInfos(self): # Méthode d'instance
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans")

    @staticmethod    
    def formater_chaine(a): # Une méthode statique : ne dépend pas du self
        return a[0].upper() + a[1:].lower()
    
    @classmethod
    def methode_de_classe(cls): #Très peu utilisé, on utilise plutot des méthodes static
        print("Méthode de classe")

    # représentation chaine
    # def __str__(self):
    #    return "STR"

    # dev
"""    def __repr__(self):
        return __class__.__name__ + " " + str(self.__dict__)"""

personne1 = Personne("Jean", 20)
personne1.AfficherInfos()

print(personne1.formater_chaine("tOto"))


# --- Modificateurs d'accès : Public, private, protected ---

class Chat:
    def __init__(self, nom):
        # public : accès depuis intérieur et extérieur de la class
        #self.nom = nom

        # private : ne jamais utiliser la variable en dehors de la class, accès intérieur only
        #self.__nom = nom

        # protected : accès depuis l'intérieur de la classe et des classes dérivées
        self._nom = nom

    def se_presenter(self):
        print(f"Je m'appelle {self._nom}")

chat1 = Chat("Zeus")
chat1.se_presenter()

print(chat1.__dict__)
