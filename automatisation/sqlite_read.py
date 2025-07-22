# --- SQLITE CREATION DE LA TABLE ---
import sqlite3

connexion = sqlite3.connect("albums2.db")
curseur = connexion.cursor()

for artiste in curseur.execute('SELECT * FROM artiste;'):
    print(artiste)
#curseur.execute('SELECT nom FROM artiste;')
"""artistes =curseur.fetchall()
print(artistes)"""

connexion.close()