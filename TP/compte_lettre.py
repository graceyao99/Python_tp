
#on entre une chaine de caractère
#on dis le nombre de fois qu'un caractère est repéter dans la chaine 

chaines = input("Entrée une chaine de caractère")
caracteres_deja_selectionne = [] 
selection = False
#compte le nombre de fois que chaque caractère est présenté dans la chaine de caractère
for i in chaines:
    caractere = i
    #je parcours mon tableau caracteres_deja_selectionne en comparant mon caractère avec les caractère deja selectionnés
    for caractere_deja_selectionne in caracteres_deja_selectionne:

        #si le caractère est deja présent on passe au caractère suivant de notre chaine de caractère
        if caractere == caractere_deja_selectionne:
            selection = True
            break
        else :
            selection = False
        
    

     #si le caractère est n'a pas été selectionné je le stocke dans mon tableau 
     #je compte le nombre de fois qu'il est repété dans ma chaine de caractère
     #je passe au caractère suivant de notre chaine de caractère
     
    if selection == False:
        caracteres_deja_selectionne.append(caractere)
        nombre = chaines.count(caractere)
        print(f"il y a {nombre} fois {caractere} dans {chaines}")




