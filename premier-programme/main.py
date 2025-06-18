#Exo 1 : premiere fonction
print("Je m'appelle Amel. ")
print("Mon c'est bien Amel")
print("")

#Exo 2 : création de variables
name = "Amel"
print(name)
print()
print("Je m'appelle " + name + ".")
print(f"Identité : {name}")
print()

"""Exo 3 : demander des données
#answer = input("Quel est ton nom ? ")
#print("Vous vous appelez " + answer + ".")"""

#Exo 4 : demqnder l'age
"""answer = input("Quel est ton nom ? ")
age = input("Quel est votre age ? ")
print("Vous vous appelez " + answer + ", vous avez " + age + " ans.")"""

#Exo 5 : les types 
nom = "Amel"
age = 24
print(type(age))
print(type(nom))
    #Attention, on ne peut pas concaténer une valeur numérique avec des chaines de caractère, on peut convertir avec la fonction str()
print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans.")

#Exo 6 : Erreur et gestion
#answer = input("Quel est ton nom ? ")
"""age = input("Quel est votre age ? ")
try:
    age_prochain = int(age) + 1
except ValueError:
    print("Erreur: vous devez rentrer un nombre")
else:
    print(f"L'an prochain vous aurez {str(age_prochain)} ans")"""

#Exo 7 : boucle while

"""n = 0
print(n)

while n < 10:
    print("Valeur de n : " + str(n))
    n = n + 1

print("Fin de la boucle")"""

"""password = ""
while not password == "TOTO":
    password = input("What is the password ? ")

print("Correct password, you can access to your account")"""

# Exo : premier programme

"""nom = ""
while nom == "":
    print("Error : name is empty, please enter a correct value")
    nom = input("What is your name ?")

age = 0
while age == 0:
    age_str = input("How old are you ? ")
    try:
        age = int(age_str)
    except: 
        print("Error: you need to enter a number type for age")

print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans.")
print(f"L'an prochain vous aurez {str(age + 1)} ans")"""

# Exo : fonction

"""def ask_years():
    age_int = 0
    while age_int == 0:
        age_str = input("How old are you ? ")
        try:
            age_int = int(age_str)
        except: 
            print("Error: you need to enter a number type for age")
    return age_int"""

"""Pour utiliser une variable en dehors de la fonction on va utiliser une variable global 
qui comme son nom l'indique va faire comprendre qu'on utilise dans une fonction une variable externe.
On peut voir un exemple ci dessous. C'est important de noter qu'on n'est plus obligé d'appeler la
fonction dans une variable après."""
"""age = 0

def ask_years():
    global age
    while age == 0:
        age_str = input("How old are you ? ")
        try:
            age = int(age_str)
        except: 
            print("Error: you need to enter a number type for age")

ask_years()"""


"""Code Finale :
def ask_name():
    answer_nom = ""
    while answer_nom == "":
        #print("Error : name is empty, please enter a correct value")
        answer_nom = input("What is your name ?")
    return answer_nom

def ask_years(person_name):
    age_int = 0
    while age_int == 0:
        age_str = input(person_name + " how old are you ? ")
        try:
            age_int = int(age_str)
        except: 
            print("Error: you need to enter a number type for age")
    return age_int

def afficher_info_perso(person_name, person_age):
    print("Vous vous appelez " + person_name + ", vous avez " + str(person_age) + " ans.")
    print(f"L'an prochain vous aurez {str(person_age + 1)} ans")

nom1 = ask_name()
nom2 = ask_name()

age1 = ask_years(nom1)
age2 = ask_years(nom2)

afficher_info_perso(nom1, age1)
afficher_info_perso(nom2, age2)"""

"""print("Vous vous appelez " + nom1 + ", vous avez " + str(age1) + " ans.")
print(f"L'an prochain vous aurez {str(age1 + 1)} ans")

print("Vous vous appelez " + nom2 + ", vous avez " + str(age2) + " ans.")
print(f"L'an prochain vous aurez {str(age2 + 1)} ans")"""


#Exo : Condition

def ask_name():
    answer_nom = ""
    while answer_nom == "":
        #print("Error : name is empty, please enter a correct value")
        answer_nom = input("What is your name ?")
    return answer_nom

def ask_years(person_name):
    age_int = 0
    while age_int == 0:
        age_str = input(person_name + " how old are you ? ")
        try:
            age_int = int(age_str)
        except: 
            print("Error: you need to enter a number type for age")
    return age_int

"""On peut ajouter une option pour les paramètres, c'est-à-dire qu'il sera optionnel comme on peut
voir avec le paramètre taille ci dessous qui à une val par défaut de 0"""
def afficher_info_perso(person_name, person_age, taille=0):
    print()
    print("Vous vous appelez " + person_name + ", vous avez " + str(person_age) + " ans.")
    print(f"L'an prochain vous aurez {str(person_age + 1)} ans")
    print("L'an prochain vous aurez %s ans" % (person_age + 1))


    # == egal
    # < inferieur
    # > supérieur
    # <= et >= inférieur ou égal et supérieur ou égal
    # True / False (boolean)
    if person_age == 1 or person_age ==2:
        print("You are a baby")
    elif person_age < 10:
        print("You are a child")
    elif person_age == 17:
        print("You are almost major")
    #elif person_age >=12 and person_age<18:
        #print("You are an adolescent")
    elif 12 <= person_age <18:
        print("You are an adolescent")
    elif person_age == 18:
        print("You are major this year, congratulation !")
    elif person_age >= 18:
        print("You are major ")
    elif person_age > 60:
        print("You are senior")
    else:
        print("You are minor")
    
    """Afficher taille"""
    """taille = 1.75 #float type"""
    if not taille == 0:
        print("Votre taille : " + str(taille) + "m")


"""nom1 = ask_name()
nom2 = ask_name()

age1 = ask_years(nom1)
age2 = ask_years(nom2)

afficher_info_perso(nom1, age1)
afficher_info_perso(nom2, age2)"""

#Exo : Boucle for

"""On créée une constante soit une variable en majuscule, à savoir que en Python officiellement
les constantes n'existe pas mais pas convention on fait comme si. 
Il est aussi important de noté qu'une constante ne devra jamais être modifié !"""
NB_PERSONNES = 1

for i in range(0, NB_PERSONNES):
    nom = "personne" +str(i+1)
    age = ask_years(nom)
    afficher_info_perso(nom, age, 1.63)


#Print sur plusieurs ligne :
print("""
      Bonjour
            Hello""")
print("toto", 20, "ans")