def initialisation():
    n = int(input("entrez un reel positif :"))
    if n < 0:
        print("erreur, retentez :")
        initialisation()
    return n

#MAIN
n = initialisation()

x = n
for i in range (n+1):
    print(x)
    x -= 1
