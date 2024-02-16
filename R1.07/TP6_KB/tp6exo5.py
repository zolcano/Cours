import unicodedata
import re

def nettoyer_texte(texte):
    texte = re.sub(r'[^a-zA-Z0-9]', '', texte)
    return texte.lower()  

def supprimer_accents(texte):
    return ''.join(c for c in unicodedata.normalize('NFD', texte) if unicodedata.category(c) != 'Mn')

def est_palindrome(texte):
    texte_propre = nettoyer_texte(texte)
    texte_propre_sans_accents = supprimer_accents(texte_propre)
    return texte_propre_sans_accents == texte_propre_sans_accents[::-1]

phrase = input("Entrez un mot ou une phrase : ")

if est_palindrome(phrase):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
