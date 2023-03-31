#Comment faire alors pour insérer des accolades 🤯 ?
#Si vous doublez les accolades, la variable ne sera pas évaluée (les accolades sont bien visibles mais on retrouve la chaîne de caractères prenom au lieu de sa valeur).

#En triplant les accolades, on a bien des accolades qui entourent la valeur associée à la variable prenom.

prenom = "Pierre"
f"Je me nomme {{prenom}}"
'Je me nomme {prenom}'
f"Je me nomme {{{prenom}}}"
'Je me nomme {Pierre}'

#pour récupérer la clé d'un dictionnaire :

profession = {'Pierre': 'ingénieur'}
phrase = f"Pierre est {profession['Pierre']}"
phrase = f'Pierre est {profession["Pierre"]}'

#Quelques options de formatage

#Il est possible de spécifier des options de formatage avancées directement à l'intérieur des accolades.

#Les options de formatages sont séparées des données par le symbole des deux-points :

f"{valeur:formatage}"

nombre = 12

# Avec format
nombre_pad = "{:04d}".format(nombre)  # 0012

# Avec un f-string
nombre_pad = f"{nombre:04d}"  # 0012

#Voici une liste non exhaustive d'options de formatage que j'utilise très souvent 👇
#'Padder' un nombre

f"{12:04d}"


#Tronquer une chaîne de caractères

phrase = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

description = f"{phrase:.60}"

