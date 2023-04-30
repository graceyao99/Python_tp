chemin = "/home/grace/Documents/practice-python/TP/tri_bulle.py"
print(chemin)
#ouvrir un fichier avec plusieur modes(r,w,d)
with open(chemin, "r") as f:
    contenu = f.read()
    print(contenu)