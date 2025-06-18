import turtle

t = turtle.Turtle()


"""i = 0
while i != 5:
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    i = i + 1"""

"""for i in range(5):
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(30)"""

def escalier(taille, nb):
    t.forward(taille)
    for i in range(nb):
        t.left(90)
        t.forward(taille)
        t.right(90)
        t.forward(taille)
        #taille = taille - 5
        taille -= 10 #on décrémente 


#escalier(30, 5)

def carre(taille):
    for i in range(4):
        t.forward(taille)
        t.right(90)

#carre(50)

def carres(taille_depart, nb):
    for i in range(nb):
        taille = (i+1) * taille_depart
        carre(taille)

carres(30, 5)
turtle.done()