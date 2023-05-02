"""Le but de cet exercice est d'enlever les doublons de la liste.

Pour réussir l'exercice, vous devez utiliser une autre méthode que celle qui consiste à convertir la liste en set pour enlever les doublons.

Vous devez donc retourner la liste suivante dans une variable resultat :"""

nombres = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]

new_nombres = [] #nouveau tableau des nombres 
selection = False

for i in nombres:
    nombre = i
    #je parcours mon tableau new_nombres en comparant mon nombre avec les nombres deja selectionnés
    for new_nombre in new_nombres:

        #si le nombre est deja présent on passe au caractère suivant de notre chaine de caractère
        if nombre == new_nombre:
            selection = True
            break
        else :
            selection = False
        
    

     #si le nombre est n'a pas été selectionné je le stocke dans mon tableau 
     #je passe au nombre suivant de notre tableau nombres
     
    if selection == False:
        new_nombres.append(nombre)
        
print(new_nombres)




