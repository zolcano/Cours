dico = {
    'firstname' : 'toto',
    'name' : 'titi',
    'promo' : 'rt11',
    'group' : 'rt112'
}

print("votre nom est",dico["name"],", prénom est ",dico["firstname"],", vous faites partie de la promo ",dico["promo"]," et votre groupe est ",dico["group"])
print("-----------")
print("Les clés du dictionnaire sont :")
for x in dico.keys():
    print("-",x)
print("Les valeurs du dictionnaire sont :")
for x in dico.values():
    print("-", x)
print("Les tuplets du dictionnaire sont :")
for x in dico.items():
    print("-", x)
print("-----------")

dico2 = {
    'firstname' : 'tata',
    'name' : 'tutu',
    'promo' : 'rt11',
    'group' : 'rt111'
}

binome = {
    '1' : 'toto',
    '2' : 'tata',
}

print("Les étudiants formants le binôme sont :")
print("- L'étudiant toto titi du groupe 202 - L'étudiant tata tutu du groupe 102")