# Polymorphisme
# plusieurs types -> la même interface (même code)

class EtreVivant:
    def afficher_infos(self):
        print("Je suis un être vivant")

class Chat(EtreVivant):
    def afficher_infos(self):
        print("Je suis un chat")

class Personne(EtreVivant):
    def afficher_infos(self):
        print("Je suis une personne")

l = [EtreVivant(), Chat(), Personne()]

for e in l:
    e.afficher_infos()

#objectif : faire fonctionner avec les int et str
def additionner(a, b):
    somme = 0
    if isinstance(a, int):
        somme += a
    if isinstance(a, str):
        somme += len(a)
    if isinstance(b, int):
        somme += b
    if isinstance(b, str):
        somme += len(b)
    return somme

print(additionner(5, "aaa"))