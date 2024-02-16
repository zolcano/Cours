def factorielle(n):
    resultat = 0
    while n>0:
        resultat += n
        n=n-1
    return(resultat)

x = int(input("entrez un reel :"))
y = factorielle(x)
print("factorielle",x,"= ",y)