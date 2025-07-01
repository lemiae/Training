
# --- La POO ---
# Difference prog impérative / objet

#Entité : Personne (entité -> class)
#   Données : nom, age
#   Actions (méthodes) : sePresenter(), DemanderNom() (input)



# --- DEFINITION ---
class Personne:
    def __init__(self, nom: str="", age: int=0): #constructeur
        self.nom = nom
        self.age = age
        if nom == "":
            self.DemanderNom()
        print("Constructeur personne " + self.nom)
    
    def SePresenter(self):
        info_perso = "Bonjour, je m'appelle " + self.nom
        if self.age != 0:
            info_perso += ", j'ai " + str(self.age) + " ans"
            print(info_perso)
        else:
            print(info_perso)
        
        if self.age != 0:
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
    def DemanderNom(self):
        self.nom = input("Quelle est ton nom ?")

# --- UTILISATION ---
#personne1 = Personne(age=20)
#personne2 = Personne("Jean", 15)

liste_personnes = [Personne(age=20), Personne("Jean", 15)]
print("Liste 1")
for personne in liste_personnes:
    personne.SePresenter()

#liste_personnes[0].SePresenter()
print("Liste 2")
personne4 = Personne(age=20)
liste_personnes.append(personne4)
for personne in liste_personnes:
    personne.SePresenter()
#personne1.SePresenter() #méthode d'instance
#personne2.SePresenter()

#Personne.AutreFonction() #méthode de classe
#print("estMajeur : ", personne1.EstMajeur())
#print("estMajeur : ", personne2.EstMajeur())


'''def afficher_info_pers(nom, age):
    print(f"LA personne s'appelle {nom}, son age est de {age} ans")

def demander_nom_pers():
    nom = input("Quel est votre nom ?")
    return nom'''

