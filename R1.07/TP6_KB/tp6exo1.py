L1 = [0] * 3
print("Liste obtenue :", L1)
print("Type de la liste :", type(L1))
print("ID de la liste :", id(L1))

for element in L1:
    print("Valeur :", element)
    print("Type :", type(element))
    print("ID :", id(element))

L1[1] += 1
print("Liste après modification :", L1)
print("Type de la liste après modification :", type(L1))
print("ID de la liste après modification :", id(L1))

for element in L1:
    print("Valeur :", element)
    print("Type :", type(element))
    print("ID :", id(element))

ma_chaine = "machaine"
print("ID de la variable ma_chaine :", id(ma_chaine))
for char in ma_chaine:
    print("Caractère :", char)
    print("Type :", type(char))
    print("ID :", id(char))
