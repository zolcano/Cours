def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

lst1 = [0, 1, 2]

lst2 = ajouter_elt(lst1, len(lst1))

print("Contenu de lst1 :", lst1)
print("Type de lst1 :", type(lst1))
print("ID de lst1 :", id(lst1))

print("\nContenu de lst2 :", lst2)
print("Type de lst2 :", type(lst2))
print("ID de lst2 :", id(lst2))