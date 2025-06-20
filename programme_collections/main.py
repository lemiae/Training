#Collections : tableaux, listes, tuples...
# Tuple (): immutable -> non modifiable et prend moins de place d'ou l'utiliser en priorité
# Liste []: mutable -> modifiable : rajouter/supprimer des éléments ou modifier plusieurs éléments

personnes = ("mélanie", "jean", "martin") # avec des parenthèses c'est un tuple, 
# le tuple est 'readonly' c'est-à-dire qu'il est fixe, on ne peut pas rajouter d'éléments

for i in range(0, len(personnes)):
    print(personnes[i])

print(personnes[-1]) # -1 pour le dernier éléments

print()
for i in personnes:
    print(i)
    print(len(i))
    print(i[0])

valeurs = range(0, 5)
print(valeurs[-1])


# Les listes :
personnes = ["mélanie", "jean", "martin"]
new_personne = "David"

print(personnes)
personnes.append(new_personne)
del personnes[1]

print(personnes)

def afficher_personne(c):
    for i in c:
        print(i)

afficher_personne(personnes)

def modifier_vale(a):
    a[0] = 10

test = [1, 2, 3, 4]
print(test)
modifier_vale(test)
print(test)

# LEs fonctions et les tuples :

def obtenir_info():
    return "mélanie", 37, 1.65

def afficher_info(nom, age, taille):
    print(f"info : nom : {nom}, age: {age}, taille: {taille}")

infos = obtenir_info()
#afficher_info(nom, age, taille)
afficher_info(*infos) # unpack le tuples


# Slices :
personnes = ("mélanie", "jean", "martin", "paul", "pierre", "jacque")

for i in personnes[0:3]: #affiche les 3 premiers
    print(i)
print()

# [start:stop:step]
for i in personnes[::2]:
    print(i)

