from random import*
vous = 50
ennemi = 50

while vous > 0 or ennemi >0 :
    saisie = int(input("Souhaitez vous attaquer(1) ou utiliser une potion(2): "))
    nombre_aleatoire_vous = randint(5,10)
    nombre_aleatoire_ennemi = randint(5,15)
    if saisie == 1:
        ennemi = ennemi - nombre_aleatoire_vous
        vous = vous - nombre_aleatoire_ennemi
        print(f"il vous reste {vous}\nil reste {ennemi} à votre ennemi ")
        continue
        