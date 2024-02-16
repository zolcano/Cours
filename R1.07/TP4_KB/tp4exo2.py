nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0

notes = []
for i in range(nombreEtudiants):
    x = "Note etudiant " + str(i) + " : "
    y = float(input(x))
    notes.append(y)

tt = 0
for i in range(nombreEtudiants):
    tt += notes[i]
moyenne = tt/nombreEtudiants
print("moyenne de classe : ", moyenne)

print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    print(i," | ", notes[i]," | ",notes[i]-moyenne)