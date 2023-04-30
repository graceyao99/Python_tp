employes = {
    "patrick":{"nom":"YAO Patrick", "age":25},
    "adjoua":{"nom":"YAO Adjoua", "age":24},
    "julie":{"nom":"YAO Julie", "age":25}
}

#enlever patrik de la liste
del employes["patrick"]
print(employes)

#changer l'age de julie
employes["julie"]["age"] = 26
print(employes)

#afficher l'age de Adjoua
age = employes["adjoua"].get("age")
print(f"Adjoua a {age}")

#Dans cet exercice, nous allons récupérer la valeur de la clé "prenom", contenue dans le dictionnaire employes.

employes = {
            "01": {
                "identite": {
                    "prenom": "Pierre",
                    "nom": "Dupont"
                    }
                }
            }

resultat = (employes["01"].get("identite")).get("prenom")
print(resultat)

#La variable names contient un dictionnaire avec plusieurs personnes qui possèdent le même nom de famille.

#Nous souhaiterions regrouper tous les gens avec le même nom de famille dans le dictionnaire 

names = {
            "Patrick": "Smith",
            "Julie": "Mercier",
            "Maxime": "Moulin",
            "Gérard": "Moulin",
            "Rose": "Mercier",
            "Clara": "Smith",
            "John": "Moulin",
            "Michel": "Smith",
        }

