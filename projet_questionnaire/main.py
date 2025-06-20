
def poser_question(question, r1, r2, r3, r4, choix_bn_reponse):
    global score
    print("Question :", question)
    print("a", r1)
    print("b", r2)
    print("c", r3)
    print("d", r4)
    reponse = input("Votre réponse : ")
    if reponse == choix_bn_reponse:
        print("Bonne réponse")
        score +=1
    else:
        print("Mauvaise réponse")

score = 0
poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
