nmax = 3

txt = "Quelle est la taille de vos vecteurs [entre 1 et " + str(nmax) + "] ? "
taille = int(input(txt))
txt = "incorrect, " + txt
while taille < 1 or taille > nmax:
    taille = int(input(txt))

v1, v2 = [], []

print("Saisie du premier vecteur :")
for i in range(taille):
    txt = "v1[" + str(i) + "] = "
    x = int(input(txt))
    while x < 1 or x > taille:
        x = int(input("incorrect : "))
    v1.append(x)

print(" ")

print("Saisie du second vecteur :")
for i in range(taille):
    txt = "v2[" + str(i) + "] = "
    x = int(input(txt))
    while x < 1 or x > taille:
        x = int(input("incorrect : "))
    v2.append(x)

y = 0
for i in range(taille):
    y += v1[i]*v2[i]

print("")
print("Le produit scalaire de v1 par v2 vaut ",y)