def initialisation():
    n = int(input("entrez un reel positif :"))
    if n < 0:
        print("erreur, retentez :")
        initialisation()
    return n

def choix():
    print("(1): -boucle while")
    print("(2) - boucle for")
    print("----")
    x = input("choisissez entre 1 et 2 :")
    x = int(x)
    print("----")
    if x != 1 and x != 2:
        print("erreur, retentez")
        choix()
    return x

def boucle1(n):
    x = 1
    while n > 1:
        x *= n
        print(x)
        n-=1
    return(x)
    
def boucle2(n):
    x = 1
    for i in range(n-1):
        x *= n
        n -= 1
        print(x)
    return(x)

#Main
n = initialisation()
x = choix()
if x == 1:
    y = boucle1(n)
    print("la factorielle de",n,"est",y)
else:
    y = boucle2(n)
    print("la factorielle de",n,"est",y)