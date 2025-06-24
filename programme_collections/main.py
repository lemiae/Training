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


# Exercice :
nom_collection = []

while True:
    name = input("What's the name of the person ?")
    if name == "":
        break
    else:
        nom_collection.append(name)

print()
print("NAme of the person :")
for name in nom_collection:
    print(" " + name)

# Exo : valeur la plus petite 
nom_chauffeur = ["Patrick", "Paul", "Marie", "Jeanne", "Marc"]
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1]
noms_distance = [("Patrick", 1.5), ("Paul", 2.2), ("Marie", 0.4)]

#V1
distance_min = distance_chauffeur_km[0]
for distance in distance_chauffeur_km:
    if distance < distance_min:
        distance_min = distance

print("Distance minimale :", distance_min)

for i in range(len(distance_chauffeur_km)):
    if distance_chauffeur_km[i] == distance_min:
        print("L'index est", i)

distance_chauffeur_km.sort()
print(distance_chauffeur_km)

#V2
distance_min = noms_distance[0]
for nom_dist in noms_distance:
    if nom_dist[1] < distance_min[1]:
        distance_min = nom_dist

print("Distance min:", distance_min[1], "Nom: ", distance_min[0])