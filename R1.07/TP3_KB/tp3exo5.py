def initialisation():
    global debut, fin
    
    x = False
    while x != True:
        debut = input("entrez l'heure de location :")
        debut = int(debut)
        if debut > 23 or debut < 0:
            print("incorrect")
        else :
            x = True
    
    y = False
    while y != True:
        fin = input("entrez l'heure de retour :")
        
        if float(fin) == int(fin):
            fin = int(fin)
        else :
            fin = int(fin)+1
            
        if fin > 24 or debut < 1:
            print("incorrect")
        else :
            y = True
    
    calcul(debut, fin)

def calcul(x, y):
    prix=0
    while y != x:
        if y > 17 or y < 7:
            prix+=1
        else:
            prix+=2
        y -= 1
    print("le prix total est :", prix,"euros")

initialisation()