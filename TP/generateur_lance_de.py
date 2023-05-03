"""Le but de cet exercice est de générer 6 lancer de dés aléatoires, allant de 1 à 6.

Votre script doit récupérer ces lancers de dés dans la variable lancers."""

import random
lancers = [] 

for i in range(5):
    n = random.randint(1, 6)
    lancers.append(n)

for lancer in lancers:
    print(lancer)