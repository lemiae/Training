
def afficher_table_multiplication(n, min=1, max=10):
    print("Table de multiplication de", n, ":")
    if min > max:
        print("Error : min must be inferior to max")
        return
    
    for i in range(min, max+1):
        resultat = i*n
        print(i, "x", n, "=", resultat)

afficher_table_multiplication(4)