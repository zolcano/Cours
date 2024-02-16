notes = []
coefficients = []

for i in range(1, 6):
    note, coefficient = map(float, input(f"Veuillez entrer la note du module {i} et le coefficient correspondant : ").split())
    notes.append(note)
    coefficients.append(coefficient)

coef = 0
moyenne = 0
for i in range(len(notes)):
    moyenne += notes[i] * coefficients[i]
    coef += coefficients[i]
moyenne /= coef

if moyenne > 10 and all(note >= 8 for note in notes):
    print("L'étudiant est admis.")
else:
    print("L'étudiant n'est pas admis.")