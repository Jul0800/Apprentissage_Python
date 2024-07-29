#Déclaration de deux variables pour stocker les deux nombres
nombre_a_gauche = 1
nombre_a_droite = 2.5

#Déclaration d'une variable résultat qui contiendra le résultat du calcul
resultat = 0

#Vérification que les deux variables sont des nombres entiers
if isinstance (nombre_a_gauche, int) and isinstance (nombre_a_droite, int):
    print ("Les deux variables sont bien des entiers")
else :
    print ("L'une des deux variables n'est pas un entier")
    exit(1)
#Déclaration d'une variable symbole pour stocker le symbole d'opération
symbole = '-'
#Vérification du symbole stocké dans la variable  symbole
match symbole:
    case "+":
        resultat = nombre_a_gauche + nombre_a_droite
        print ("Voici le résultat de l'opération :", resultat)
    case "-":
        resultat = nombre_a_gauche - nombre_a_droite
        print ("Voici le résultat de l'opération :", resultat)
    case "*":
        resultat = nombre_a_gauche * nombre_a_droite
        print ("Voici le résultat de l'opération :", resultat)
    case "/":
        if nombre_a_droite !=0:
            resultat = nombre_a_gauche / nombre_a_droite
            print ("Voici le résultat de l'opération :", resultat)
        else:
            print ("Mauvais calcul, un nombre ne peut pas être divisé par O, le nombre à droite doit être supérieur à 0")
            exit (1)
    case _:
        print ("Le symbole d'opération n'est pas connu")
