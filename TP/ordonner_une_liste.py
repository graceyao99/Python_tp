"""Le but de cet exercice et de remettre en ordre alphabétique les prénoms présents dans la chaîne de caractères.

Vous devez créer une variable chaine_en_ordre qui, à la fin de l'exercice, doit contenir la chaîne de caractères suivante :

"Adjoua, Anne, Julien, Lucien, Marie, Pierre" """

chaine = "Pierre, Julien, Anne, Marie, Lucien, Adjoua"
chaine_en_ordre =""

tableau_chaine = chaine.split(", ")

#mon module tri-bulle
tri = False
plus_grand = 0
borne = len(tableau_chaine)

while tri == False:
    tri = True
    for i in range(borne-1):
        if tableau_chaine[i] > tableau_chaine[i+1] :
            plus_grand = tableau_chaine[i]
            tableau_chaine[i] = tableau_chaine[i+1]
            tableau_chaine[i+1] = plus_grand
            tri = False

print(tableau_chaine) 
 #terminaison
chaine_en_ordre = ", ".join(tableau_chaine)
print(chaine_en_ordre)



