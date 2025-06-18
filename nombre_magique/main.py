import random

def demander_nombre(nb_min, nb_max):
    nbr_int = 0
    
    while nbr_int == 0:
        nbr_magique = input(f"Quel est le nombre magique ? Il doit etre compris entre {nb_min} et {nb_max}. ")
        try:
            nbr_int = int(nbr_magique)
        except: 
            print("Error: you need to enter a number type for magic number")
        else:
            if nbr_int < nb_min or nbr_int > nb_max:
                print(f"Erreur : le nombre doit être entre {nb_min} et {nb_max}. Réessayez")
                nbr_int = 0
    return nbr_int

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(1, 10)
NOMBRE_VIES = 4

nombre = 0
vies = NOMBRE_VIES
while not nombre == NOMBRE_MAGIQUE and vies > 0:
    print(f"Il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné")
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
        vies -= 1
    else:
        print("Le nombre magique est plus grand")
        vies -= 1
if vies == 0:
    print(f"Vous avez perdue ! le nombre magique était : {NOMBRE_MAGIQUE}")