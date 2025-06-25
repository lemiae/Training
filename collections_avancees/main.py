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