from random import randrange
valeur = randrange(0, 100)

print("la valeur est :", valeur)

if valeur > 50:
    print("Pile!")
else:
    print("Face!")