# Les collections : Listes / Tuples
# --- Append / Extend / += / Insert ---

noms = ["Jeans", "Sophie", "Martin"]

noms_supp = ["Christophe", "Zoe"]

#noms.append("Toto") # insert un seul item ! 

# noms.extend(noms_supp) # peut insérer plusieurs éléments comme par exemple une liste dans une autre liste

#noms += noms_supp # ajoute comme le extend

#noms.insert(1, "Toto") # insérer à une certaine position

noms = noms_supp + noms #on peut concaténer des listes

print(noms)

# --- Les slices ---

slices_noms = noms[:] #permet également de faire une copie, on créee une nouvelle liste ! 
slices_noms = noms[:-1]

slices_noms[0] = "Toto"

print(noms[:]) # prend toute la liste
print(slices_noms)
print()

# --- Tris : sort / sorted ---

#noms.sort() # inplace, on remplace la liste par celle trié
noms.sort(key=lambda nom : len(nom), reverse=True)

noms_tries = sorted(noms) #permet de préserver la liste de base 

print(noms)
print(noms_tries)

# --- Opérations sur les éléments : min, max, in, sum ---

ages = [21, 20, 30, 25, 22]

print(max(ages))
print(min(noms)) #sur les chaines de caractère affiche le nom avec l'ordre alphabétique le plus proche de A

if "Jeans" in noms:
    print("Présent")
else:
    print("Absent")

print(sum(ages))

# --- Swapper deux éléments ---

"""t = noms[0]
noms[0] = noms[2]
noms[2] = t"""

noms[0], noms[2] = noms[2], noms[0] #permuter deux éléments ou plus, on peut autant qu'on veut

print(noms)

# --- Join et Split ---

#Join : rejoindre, coller

nom_join = ", ".join(noms)
print(nom_join)

#Split : séparer

nom_split = nom_join.split(", ")
print(nom_split)


# --- Index, Find et Count ---

print(noms.index("Martin"))
element_chercher = "Martin"
nb_occurences = noms.count(element_chercher)

if nb_occurences > 0:
    index_occurence = 0
    for i in range(nb_occurences):
        index_occurence = noms.index(element_chercher, index_occurence)
        print(element_chercher, "trouvé à", index_occurence)
        index_occurence += 1
else:
    print("Pas d'élément")

a = "Jean-Martin-Toto"
i = a.find("Martin")
print(i)

# --- Les compréhension de listes ---

"""longeur_noms = []
for nom in noms:
    longeur_noms.append(len(nom))"""

longeur_noms = [len(nom) for nom in noms if len(nom) < 10] # compréhension de liste c'est une syntaxe plus concise 
noms_avec_e = [e for e in noms if "e" in e]
longeur_noms = [len(nom) if len(nom) < 10 else 0 for nom in noms]
a = [i for i in range(5) if (i//2)*2 == i] #nombre pair et impaire avec !=
b = [True if (i//2)*2 == i else False for i in range(11)]

print(longeur_noms)
print(noms_avec_e)
print(a)
print(b)

# --- Any et All ---

a = [True, False, True, True]
print(any(a)) #au moins un élément vrai 
print(all(a)) # tout vrai si affiche false

noms_avec_z = any([True if "z" in nom.lower() else False for nom in noms])
print(noms_avec_z)

# --- Any / isdigit ---
print()
def chaine_contient_chiffre(chaine):
    """for c in chaine:
        if c.isdigit():
            return True
    return False"""
    return any([c.isdigit() for c in chaine])

nom = input("Quel est ton nom ?")
if nom == "":
    print("Vide")
elif chaine_contient_chiffre(nom):
    print("ce nom contient des chiffres")
else:
    print("Bonjour " + nom)


print("a".isdigit()) #vérifie si c'est que un chiffre

nom = "toto12"
"""print(chaine_contient_chiffre(nom))"""

digits = any([c.isdigit() for c in nom])
print(digits)

# --- In insensible à la casse ---

def element_dans_liste(e, l):
    l_lower = [el.lower() for el in l]
    return e.lower() in l_lower

if element_dans_liste("JEans", noms):
    print("Jean est là")
else:
    print("Jean n'est pas là")
