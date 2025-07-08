import copy

# --- La POO ---
# Difference prog impérative / objet

#Entité : Personne (entité -> class)
#   Données : nom, age
#   Actions (méthodes) : sePresenter(), DemanderNom() (input)



# --- DEFINITION ---
class EtreVivant: # class parent
    ESPECE_ETRE_VIVANT = "(Etre vivant non Identifié)"

    def AfficherInfoEtreVivant(self):
        print("Infos être vivant :" + self.ESPECE_ETRE_VIVANT)


class Chat(EtreVivant): # Notion d'héritage, class enfant
    ESPECE_ETRE_VIVANT = "Chat (Mammifère félin)"



class Personne(EtreVivant): # class enfant
    ESPECE_ETRE_VIVANT = "Humain (Mammifère Homo sapiens)" # variable de classe (1 pour toute la classe), pratique pour faire des modif de tous le monde d'un coup

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
    
    def __eq__(self, other):# Avec ça on peut comparer deux objets mais ici avec leur valeur
        if self.nom == other.nom and self.age == other.age:
            return True
        return False

class Etudiant(Personne):
    def __init__(self, nom: str, age: int, etudes: str): #constructeur
        super().__init__(nom, age)
        self.etudes = etudes
    
    def SePresenter(self):
        super().SePresenter()
        print("Je suis etudiant en " + self.etudes)
        #return super().SePresenter()


# --- UTILISATION ---
#personne1 = Personne(age=20)
#personne2 = Personne("Jean", 15)

liste_personnes = [Personne("Jean", 20), 
                   Personne("Jean", 15)]
print("Liste 1")
for personne in liste_personnes:
    personne.SePresenter()

#liste_personnes[0].SePresenter()
print("Liste 2")
personne4 = Personne(age=20)
liste_personnes.append(personne4)
for personne in liste_personnes:
    personne.SePresenter()
    personne.AfficherInfoEtreVivant()


chat = Chat()
chat.AfficherInfoEtreVivant()

etudiant = Etudiant("Leila", 19, "informatique")
etudiant.SePresenter()
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

personne1 = Personne("Jacque", 30)
personne2 = Personne("Michel", 29)
personne1.SePresenter()

personne2 = copy.copy(personne1) #On peut aussi utilise deepcopy pour faire une copy plus poussé
personne2.SePresenter()
# Pour comparer deux personnes on peut utiliser le is :
# PAr défaut il compare les objets, pas les valeurs entré
print(personne1 is personne2)



