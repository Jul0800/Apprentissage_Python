#Création d'un dictionnaire

campagne_marketing= {
    "responsable_de_campagne" : "Jean Dupont",
    "nom_de_campagne" : "Running Love",
    "date_de_début" : "21/07/2024",
    "date de fin" : "30/07/2024"
    }

#Création d'un dictionnaire 2
Chaussures_running = {}
Chaussures_running['Asics']=1
Chaussures_running['Nike'] = 2
Chaussures_running['Saucony']=3

#Accédez à une valeur dans un dictionnaire
#print (campagne_marketing ["responsable_de_campagne"])
#print (Chaussures_running["Asics"])

Chaussures_running['New Balance']= 'préféré des français' #nous avons rajouté une nouvelle valeur au dictionnaire

#print (Chaussures_running.keys()) #retourne une vue sur les clé du dictionnaire
#print (Chaussures_running.items()) # retourne une vue sur les items c'est à dire les paires clés-valeurs

del Chaussures_running["Saucony"] #on a supprimé la clé-valeur saucony du dictionnair
#print (Chaussures_running)
#print (campagne_marketing.get("responsable_de_campagne")) #retourne la valeur associée à la clé spécifiée

print ("date_mi_campagne" in campagne_marketing) #Vérifie l'existence d'une clé spécifiée. Retourne une valeur booléen


