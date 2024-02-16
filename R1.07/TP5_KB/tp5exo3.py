def palindrome(chaine):
    chaine = chaine.lower()
    chaine = chaine.replace(" ", "")
    return chaine == chaine[::-1]

# Exemple d'utilisation
chaine = input("Entrez une chaîne de caractères : ")
if palindrome(chaine):
    print("La chaîne est un palindrome.")
else:
    print("La chaîne n'est pas un palindrome.")
