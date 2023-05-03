"""Dans cet exercice, nous allons vérifier si une phrase est un palindrome ou non.

Un palindrome est un mot ou une phrase qui peut se lire de la même façon dans les deux sens.
Votre script devra donc vérifier si cette phrase est un palindrome, et donc dans ce cas-ci, retourner la valeur True dans la variable resultat."""

mot = "Un roc cornu"
mot = mot.lower()
mot = mot.strip()
print (mot)
tableau_lettre =[]
for lettre in mot:
    tableau_lettre.append(lettre)
print(tableau_lettre)