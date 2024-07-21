"""
print ("J'apprends Python!")
resultat = (17+35 )* 2
Utilisateur = "Julius"
print (f"Bonjour {Utilisateur}, {resultat} est le résultat du calcul ") ##Utilisation de f-string 

"""
"""
nom= "Fayihoun"
age= 24
age=age+10
print (f"Bonjour, je m'appelle {nom} et j'ai {age} ans")
"""
""""
#Exercice sur les types de données 
nom= "Fayihoun"
age= 25
taille= 1.77
est_etudiant = True

print (f"nom est {nom}")
print (f"age est {age}")
print (f"taille correspond à {taille}")
print (f"{nom} est étudiant {est_etudiant}")

print (f"La variable nom est de type {type(nom)}")
print (f"La variable age est de type {type(age)}")
print (f"La variable taille est de type {type(taille)}")
print (f"La variable est_etudiant est de type {type(est_etudiant)}")
"""

#Utilisation de la fonction type(nom de la variable) pour déterminer le type de 
#la variable

#Utilisation des listes dans Python
"""
plateformes_sociales =["Facebook","Twitter","Instagram","TikTok","Facebook Messenger"]
plateformes_sociales[2]= "Linkedin" #à ce niveau, on a créé une nouvelle valeur dans la liste en remplaçant Instagram par Linkedin
print(plateformes_sociales) # on affiche la nouvelle liste

"""

#Ajoutez, retirez, triez des listes 
#Rajouter le réseaux thread à la fin de la liste existante
""""
plateformes_sociales.append("Thread")
print(plateformes_sociales)

"""
#Pour retirer un élément d'une liste on utilisera remove
""""
plateformes_sociales.remove("Thread")
print(plateformes_sociales)

"""

#Connaître la longueur de la liste en utilisant len()
#len(plateformes_sociales)

#Trier les éléments d'une liste avec sort
""""
plateformes_sociales.sort() #Le trie se fait de façon alphabétique
print(plateformes_sociales)

"""
#langage = "PYTHON"
#langage[2] #Accéder aux caractères d'une chaîne 
#comme un élément d'une liste

#Différence entre tuples et listes
#mon_tuple = (1,2,3,4) #je définis la variable tuple
#print (mon_tuple)
#mon_tuple [2]= 5 #Test de l'immuabilité des tuples. 
#Message d'erreur qui signale qu'on ne peut pas modifier une nouvelle valeur

#On déclare une nouvelle variable
#mon_tuple_bis =(5, "six", "sept", "huit")

#nouveau_tuple = mon_tuple + mon_tuple_bis #concaténation des deux anciennes variables
#print (nouveau_tuple)

#Savoir si un élément est présent dans une liste ou un tuple
#fonction in

#5 in mon_tuple_bis

# Utilisation des dictionnaires pour enregistrer des données complexes
#Paire "clé" "valeur"



