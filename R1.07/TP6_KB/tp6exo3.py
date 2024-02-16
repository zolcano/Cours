def ajouter_elt(lst=[0,1,2], elt=3):
    lst.append(elt)
    return lst

print(ajouter_elt())
print(ajouter_elt())

print("ID de lst lors du premier appel :", id(ajouter_elt()))
print("ID de lst lors du deuxième appel :", id(ajouter_elt()))

def ajouter_carac(ch="abc", elt="d"):
    return ch + elt

print(ajouter_carac())
print(ajouter_carac())

print("ID de ch lors du premier appel :", id(ajouter_carac()))
print("ID de ch lors du deuxième appel :", id(ajouter_carac()))
