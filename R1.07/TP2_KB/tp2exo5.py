x = int(input("entrez un réel :"))

if x < 0:
    nombre = "négatif"
elif x == 0:
    nombre = "zero"
else:
    nombre = "positif"

if x%2 == 0:
    parite = "pair"
else:
    parite = "impair"

print("le nombre est",nombre,"et il est",parite)


