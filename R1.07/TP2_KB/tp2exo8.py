while True:
    I = "[2,3[ U ]0,1] U [-10,-2]"
    print("I =",I)

    x = float(input("entrez un reel :"))

    y = 0
    if (x < 3 and x > 2 or x == 2) or (x > 0 and x < 1 or x == 1 ) or (x > -10 and x < -2 or x == -10 or x ==-2):
        print(x, "appartient à I")
        y = y + 1

    if y == 0:
        print(x, "n'appartient à aucun intervalle défini.")