from random import randrange
def initialisation(t):
    l = []
    for i in range(t):
        l.append(randrange(0,9))
    return(l)

def tri(l):
    print(l)
    for i in range(len(l)):
        x = len(l)-1
        while x != -1:
            if l[i] > l[x]:
                l[i],l[x] = l[x],l[i]
            x -= 1
        print(l)
    l.insert(0, l[len(l)-1])
    del(l[len(l)-1])
    print(l)



#MAIN
taille = randrange(5, 10) #taille de la liste
liste = initialisation(taille) #création de la liste

listetemp = liste
tri(listetemp)
print("--------------")
print(sorted(liste))
print("la fonction sorted trie la liste dans l'ordre croissant")
print("--------------")
print(liste.sort())