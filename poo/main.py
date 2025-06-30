
# --- La POO ---
# Difference prog impérative / objet

#Entité : Personne (entité -> class)
#   Données : nom, age
#   Actions (méthodes) : sePresenter(), DemanderNom() (input)



# --- DEFINITION ---
class Personne:
    def __init__(self, nom: str, age: int): #constructeur
        self.nom = nom
        self.age = age
        print("Constructeur personne " + nom)
    
    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        if self.EstMajeur():
            print("Je suis majeur")
        else:
            print("Je suis mineur")
    
    def AutreFonction():
        print("Autre fonction")
    
    def EstMajeur(self):
        return self.age >= 18
        """if self.age >= 18:
            return True
        else:
            return False"""

# --- UTILISATION ---
personne1 = Personne("Toto", 30)
personne2 = Personne("Jean", 15)

personne1.SePresenter() #méthode d'instance
personne2.SePresenter()

Personne.AutreFonction() #méthode de classe
print("estMajeur : ", personne1.EstMajeur())
print("estMajeur : ", personne2.EstMajeur())


'''def afficher_info_pers(nom, age):
    print(f"LA personne s'appelle {nom}, son age est de {age} ans")

def demander_nom_pers():
    nom = input("Quel est votre nom ?")
    return nom'''

