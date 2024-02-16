def taille_chaine(chaine):
    return len(chaine)

def pourcentage_voyelles(chaine):
    taille = taille_chaine(chaine)
    voyelles = "aeiouAEIOU"
    nb_voyelles = sum(1 for char in chaine if char in voyelles)
    return (nb_voyelles / taille) * 100 if taille > 0 else 0

def recherche_sous_chaine(chaine, sous_chaine):
    return chaine.find(sous_chaine)

def occurrences_sous_chaine(chaine, sous_chaine):
    count = 0
    index = chaine.find(sous_chaine)
    while index != -1:
        count += 1
        index = chaine.find(sous_chaine, index + 1)
    return count

phrase = str(input("Entrez une phrase : "))
taille = taille_chaine(phrase)
print("Taille de la chaîne :", taille)

pourcentage = pourcentage_voyelles(phrase)
print("Pourcentage de voyelles :", pourcentage, '%')

index = recherche_sous_chaine(phrase, "wagon")
if index != -1:
    print("La sous-chaîne 'wagon' commence à l'index :", index)
else:
    print("La sous-chaîne 'wagon' n'a pas été trouvée.")

occurrences = occurrences_sous_chaine(phrase, "wagon")
print("Nombre d'occurrences de la sous-chaîne 'wagon' :", occurrences)
