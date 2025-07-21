# --- FICHIER TEXTE ---

#ouvrir (open) 
#ecrire (write) -> w
#fermer (close)

#f = open("mon_fichier.txt", "w")
#f.write("Bonjour tout le monde ! \n")
import os.path

# os.mkdir("projets_python") -> créer un dossier
# os.rmdir("projets_python") -> supprimer un dossier

filename = os.path.join("projets_python", "mon_fichier.txt")
if os.path.exists(filename):
    print("Le fichier existe")
    f = open(filename, "r")
    texte = f.read()
    print(texte)
    f.close()
else:
    print("Le fichier n'existe pas")


"""try:
    f = open("mon_fichier.txt", "r")
except FileNotFoundError:
    print("ERREUR : Le fichier n'a pas pu etre ouvert")
else:
    texte = f.read()
    print(texte)
    f.close()"""

"""texte = f.read()
texte = f.readline()
print(texte)

for line in f:
    print(line, end="")

f.close()"""


# --- MANIPULER DES DONNÉES STRUCTURÉES JSON ---
import json 

personne = {
    "nom": "Amel",
    "age": 24,
    "amis" : ["Alice", "Bob", "Charlie"]
}

# On va sérialiser les data -> TXT "" (json) : dumps
# Désérialiser TXT (json) -> data : loads

personne_json = json.dumps(personne)
print(personne_json)

f = open("personne.json", "w")
f.write(personne_json)
f.close()

personne = json.loads(personne_json)
print(personne)

# --- SQLITE CREATION DE LA TABLE ---
import sqlite3

connexion = sqlite3.connect("albums2.db")
curseur = connexion.cursor()

curseur.execute("""CREATE TABLE artiste (
    artiste_id INTEGER NOT NULL PRIMARY KEY, 
    nom VARCHAR);""")

curseur.execute("""CREATE TABLE album (
    album_id INTEGER NOT NULL PRIMARY KEY, 
    artiste_id INTEGER REFERENCES artiste,
    titre VARCHAR,
    annee_sortie INTEGER);""")

curseur.execute('INSERT INTO artiste (nom) VALUES ("Michael Jackson");') # 1
mj_id = curseur.lastrowid
curseur.execute('INSERT INTO artiste (nom) VALUES ("Celine Dion");')     # 2
cd_id = curseur.lastrowid

curseur.execute('INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (' + str(mj_id) + ', "Thriller", 1982);')
curseur.execute('INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (' + str(cd_id) + ', "Falling into You", 1996);')
curseur.execute('INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (' + str(cd_id) + ', "Let\'s Talk About Love", 1997);')

connexion.commit()
connexion.close()
