def initialiser():
    n = int(input("entrez un reel superieur à 1 :"))
    if n < 1:
        print("erreur, retentez :")
        initialiser()
    return n

def suite(x):
    print("x :", x)
    tmp = 0
    n = 0
    while n < x:
        n += tmp
        tmp += 1
    return (tmp-1)

#MAIN
x = initialiser()
print("le nombre N recherché est : ",suite(x))
