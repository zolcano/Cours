#BASE
base = 4
fromage = 800
eau = 2
ail = 2
pain = 400

personne = int(input("Entrez le nombre de personne(s) conviées à la fondue :"))

print("Pour faire une fondue fribourgeoise pour", personne, "personnes, il vous faut :")
print("- ",(fromage * personne / base), "gr de fromage")
print("- ",(eau * personne / base), "Litre.s d'eau")
print("- ",(ail * personne / base), "gousse d'ail")
print("- ",(pain * personne / base), "gr de pain")
