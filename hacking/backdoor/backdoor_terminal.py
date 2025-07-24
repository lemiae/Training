# --- CREER UN TERMINAL ---
import subprocess
import os

#run : executer la commande et attendre le résultat
#resultat =subprocess.run("dir", shell=True, capture_output=True, universal_newlines=True)

#print(resultat.stdout.decode("utf-8", errors="ignore"))
#print(resultat.stdout)

# Popen : ancienne interface
# run : executer la commande et attendre le résultat

# os.getcwd()
# os.chdir(...)

while True:
    commande = input(os.getcwd() + " > ")
    if commande == "exit":
        break

    commande_split = commande.split(" ")
    if len(commande_split) == 2 and commande_split[0] == "cd":
        try:
            os.chdir(commande_split[1])
        except FileNotFoundError:
            print("ERREUR : ce répertoire n'exite pas")
    else:
        resultat = subprocess.run(commande, shell=True, capture_output=True, universal_newlines=True)  # dir sur PC

        print(resultat.stdout)
        print(resultat.stderr)