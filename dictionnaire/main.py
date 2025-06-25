# --- Partie 1 Dictionnaire ---

personne = {'nom': 'Mélanie', "age": 25, "taille": 1.60}
print(personne)

print(personne['nom'])

personne['nom'] = "Claire"
print(personne)

personne['poste'] = "Développeur"
print(personne)

achat = ("Chocolat", "Beurre")
personne['achats'] = achat
print(personne)

for i in personne:
    print(f"clef: {i}")
    print(personne[i])

# --- Partie 2 ---

personnes = [
    ("Mélanie", 25, 1.6),
    ("Paul", 29, 1.8),
    ("Jacques", 35, 1.75),
    ("Martin", 16, 1.65)
]

def obtenir_info(nom, liste): #Chercher un nom
    for i in liste:
        if i[0] == nom:
            return i
    return None

infos = obtenir_info("Jacques", personnes)
#print(infos)
personnes_dict = {
    "Mélanie": (25, 1.6),
    "Paul": (29, 1.8),
    "Jacques": (35, 1.75),
    "Martin": (16, 1.65)
 }

infos = personnes_dict.get("Claire")
# infos = personnes_dict["Jacques"]
print(infos)