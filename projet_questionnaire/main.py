
def demander_rep_numerique_user(min, max):
    reponse_str = input("Votre réponse (entre "+ str(min)+" et "+str(max)+ ") :")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int
        print("Erreur : vous devez rentrer un nombre entre", min, " et ", max)
    except:
        print("Erreur : Rentrez uniquement des chiffres")
    return demander_rep_numerique_user(min, max)

def poser_question(question):
    titre_question = question[0]
    choix = question[1]
    choix_bn_reponse = question[2]

    print("Question :", titre_question)
    for i in range(len(choix)):
        print(" ", i+1," - ", choix[i])

    #reponse_str = input("Votre réponse (entre 1 et "+str(len(choix))+ ") :")
    resultat_reponse_correcte = False
    reponse_int = demander_rep_numerique_user(1, len(choix))

    if choix[reponse_int-1].lower() == choix_bn_reponse.lower():
        print("Bonne réponse")
        resultat_reponse_correcte = True
    else:
        print("Mauvaise réponse")
    print()
    return resultat_reponse_correcte


def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score +=1
    print("Score final :", score, "/", len(questionnaire))

"""question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
question2 = ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")"""
#poser_question(question1)

questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")
    )

lancer_questionnaire(questionnaire)


#poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
