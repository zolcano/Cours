def selection(x):
    global valeurs
    x = int(input("entrez un reel entre 0 et 20 inclus :"))
    if x < 0 or x > 20:
        print("incorrect, retentez : ")
        selection(x)
    return(x)


def inferieur(x):
    y = 0
    for i in range(len(x)):
        if x[i] < 10:
            y += 1
    return(y)

def superieur(x):
    y = 0
    for i in range(len(x)):
        if x[i] >= 10 and x[i] < 15:
            y += 1
    return(y)

def superieurdeux(x):
    y = 0
    for i in range(len(x)):
        if x[i] >= 15:
            y += 1
    return(y)

#MAIN
valeurs = [0]*20

for i in range(len(valeurs)):
    valeurs[i] = selection(i)
print(valeurs)

print("Le nombre de valeurs inférieur strictement à 10 est :",inferieur(valeurs))
print("Le nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15 est :", superieur(valeurs))
print("Le nombre de valeurs supérieur ou égale à 15 est : ",superieurdeux(valeurs))