# les fonctions

"""nom = "amel"
print("Je m'appelle" + nom) # concaténer la chaine <- 1 seul paramètre
print("Je m'appelle", nom) # <- avec la virgule et comme c'est une fct ici on passe 2 paramètres

name = input("Votre nom :") # <- fct qui retourne une valeur
print("Votre nom est :", name)

# les fct permettent d'éviter de dupliquer du code <- on va factoriser le code.
nom1 = input("Nom personne 1: ")
age1 = input("Age personne 1: ")
print("le nom comporte", len(nom1), "lettres")

def est_majeur(age):
    if age >= 18:
        return True
    return False

def afficher_info_perso(nom_personne="", age_personne=0): # fct avec 2 paramètres optionnel
    if nom == "":
        print("Vous n'avez pas donné de nom, l'age vaut", age_personne)
        return
        # return <- le return fais sortir immédiatement meme si il y a du code après.
    if age_personne == 0:
        print("La personne est", nom_personne)
    else:
        print("La personne est", nom_personne, "son age est de", age_personne)
    if est_majeur(age_personne):
        print("il est majeur")
    else:
        print("il est mineur")

    print("Le nom comporte", len(nom_personne), "lettres")

age = 0
if age == 0:
    exit(0)

afficher_info_perso("toto", "20") # appel de la fonction
print("est majeur", est_majeur(18))"""

def recuperer_et_afficher_info_personne(numero_personne):
    nom = input("Nom de la personne" + numero_personne + ": ")
    age = input("Age de la personne" + numero_personne + ": ")
    print("la personne est", nom, "son age est de", age, "ans")
    print("Cette personne porte le numero ", numero_personne)

recuperer_et_afficher_info_personne(1)
