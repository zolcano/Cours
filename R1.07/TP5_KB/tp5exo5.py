def calculer_salaire(heures_travaillees, salaire_horaire):
    if heures_travaillees <= 160:
        salaire = heures_travaillees * salaire_horaire
    elif heures_travaillees <= 200:
        salaire = 160 * salaire_horaire + (heures_travaillees - 160) * salaire_horaire * 1.25
    else:
        salaire = 160 * salaire_horaire + 40 * salaire_horaire * 1.25 + (heures_travaillees - 200) * salaire_horaire * 1.5
    return salaire

heures_travaillees = int(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))
salaire = calculer_salaire(heures_travaillees, salaire_horaire)

print(f"Le salaire de l'ouvrier est de {salaire} euros.")
