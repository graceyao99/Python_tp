tableau = []
while True:
    choix = int(input("Choisissez entre les 5 options:\n1: Ajouter un élement à la liste \n2: Rétirer un élement à la liste \n3: Affichez la liste \n4: Vider la liste \n5: Modifier un élement de la liste\n6: Quitter\nVotre choix: "))

    if choix == 1:
        saisie = input("Entrez le nom de l'élement que vous voulez ajouter : ")
        tableau.append(saisie)
        continue

    elif choix == 2:
        saisie = input("Entrez le nom de l'élement que vous voulez rétirer : ")
        if saisie in tableau:
            tableau.remove(saisie)
        else:
            print("cet élement n'existe pas dans la liste")
        continue

    elif choix == 3:
        print("les élements sont:")
        for i,nom in enumerate(tableau):
            numero = i+1
            print(f"{numero}. {nom}\n")
        continue

    elif choix == 4:
        tableau.clear()
        print("la liste est vide")
        continue
    
    elif choix == 5:
        saisie = input("Entrez le nom de l'élement que vous voulez changez: ")
        if saisie in tableau:
            saisie2 = input("Entrez le nom du nouveau élement: ")
            saisie.replace(saisie, saisie2)
        else:
            print("cet élement n'existe pas dans la liste")
        continue

    elif choix == 6:
        break
    else:
        print("Saisie invalid")
        continue