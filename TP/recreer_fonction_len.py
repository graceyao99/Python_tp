#Dans cet exercice, nous allons recréer la fonction len qui permet de compter la longueur d'une variable.

def longueur(variable):
	compte = 0
	for nombre in variable:
		compte += 1
	return compte

resultat = longueur("bonjour")
print(resultat)