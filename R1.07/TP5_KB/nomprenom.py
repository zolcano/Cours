l=[]
for i in range(2):
    l.append(str(input(f"entrez le nom de la personne {i+1}:")))
    l.append(str(input(f"entrez le prénom de la personne {i+1}:")))

print("-----------")
print(str.capitalize(l[1]), str.upper(l[0]))
print(str.capitalize(l[3]), str.upper(l[2]))