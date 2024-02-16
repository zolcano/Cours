from random import randrange

def jeu(x):
    n = -1
    while n != x:
        n = int(input("entrez un nombre :"))
        if n > x:
            print("le nombre est plus petit")
        if n < x:
            print("le nombre est plus grand")
    print("vous avez trouvé, bien joué!")

#MAIN
mystere = randrange(0,100)
jeu(mystere)
