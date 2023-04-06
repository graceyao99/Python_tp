tableau = [1,5,4,2,9]
tri = False
plus_grand = 0
borne = len(tableau)

while tri == False:
    tri = True
    for i in range(borne-1):
        if tableau[i] > tableau[i+1] :
            plus_grand = tableau[i]
            tableau[i] = tableau[i+1]
            tableau[i+1] = plus_grand
            tri = False

print(tableau)        
