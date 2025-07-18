# --- UPDATE 3.9 ---

# --- UNION DE DICTIONNAIRES ---

dico1 = {"a": 1, "b": 2, "c": 3}
dico2 = {"d": 4, "e": 5, "f": 6}

#dico3 = dico1 | dico2
dico1 |= dico2
#dico3 = {**dico1, **dico2}
print(dico1)

# --- ANNOTATIONS ---
from typing import Annotated

def imc(poids: Annotated[float, "kg"], taille: float) -> float:
    return poids / (taille * taille)

print(imc(80, 1.80))
print(imc.__annotations__)

# --- SUPPRIMER PR2FIXE ET SUFFIXE D'UNE CHAINE ---

phrase = "jean a mangé un gateau"

#print(phrase.strip("gateau"))
print(phrase.removeprefix("gateau"))
p = phrase.removesuffix("jean")
print(p)

# --- UPDATE 3.10 ---

# --- CORRESPONDANCE STRUCTURELLE ---

phrase2 = input("Parlez moi :")
match phrase:
    case "bonjour" | "hello":
        print("Bonjour, comment allez vous ?")
    case "bien":
        print("je vais bien")

personne1 = {"nom": "Jean", "infos": (30, "Ingénieur informatique")}
personne2 = {"nom": "Emilie", "age": 25}

personnes = (personne1, personne2)

for personne in personnes:
    match personne:
        case {"nom": nom, "infos": (age, profession)}:
            print(f"Je m'appelle {nom}, j'ai {age} ans et je suis {profession}")

# --- MESSAGES D'ERREUR ---
