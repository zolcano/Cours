nom='toto'
prenom = "titi"
math = 13
anglais = 12
info = 12.5
promotion = 2023

print("type :",type(nom), type(prenom), type(math), type(anglais), type(info), type(promotion))

moyenne = (math +anglais +info) / 3
print("L'étudiant {} {} de la promotion {} a une moyenne de {}".format(nom, prenom, promotion, moyenne))