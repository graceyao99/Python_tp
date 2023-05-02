def add(a, b):
    try:
        return a+b
    except ValueError:
        return("les deux valeurs doivent etre des nombres")

print(add(10, "adq"))