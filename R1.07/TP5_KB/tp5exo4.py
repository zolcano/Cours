def decomposer_somme(somme):
    billets = [100, 50, 10]
    pieces = [2, 1]
    decompose = []

    for billet in billets:
        nb_billets = somme // billet
        somme -= nb_billets * billet
        decompose.append((nb_billets, billet))

    for piece in pieces:
        nb_pieces = somme // piece
        somme -= nb_pieces * piece
        decompose.append((nb_pieces, piece))

    return decompose

somme = int(input("Entrez une somme d'argent : "))
decompose = decomposer_somme(somme)

print(f"{somme} euros, c'est donc ", end="")
for nb, valeur in decompose:
    if valeur >= 10:
        print(f"{nb} billets de {valeur}, ", end="")
    else:
        print(f"{nb} pièces de {valeur}, ", end="")
print("fin.")
