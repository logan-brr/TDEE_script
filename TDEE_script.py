def calcul_bmr_tdee_objectif():
    print("=== Calcul du BMR + TDEE + Objectif ===")

    # Données de base
    sexe = input("Sexe (H/F) : ").strip().upper()
    age = float(input("Âge (en années) : "))
    poids = float(input("Poids (en kg) : "))
    taille = float(input("Taille (en cm) : "))

    # Niveau d'activité
    print("\nChoisissez votre niveau d'activité :")
    print("1 - Sédentaire (aucun sport)")
    print("2 - Léger (1-3 entraînements / semaine)")
    print("3 - Modéré (3-5 entraînements / semaine)")
    print("4 - Intense (6-7 entraînements / semaine)")
    print("5 - Très intense (2 entraînements / jour)")
    choix = input("Votre choix (1-5) : ").strip()

    niveaux = {
        "1": 1.2,
        "2": 1.375,
        "3": 1.55,
        "4": 1.725,
        "5": 1.9
    }

    if choix not in niveaux:
        print("Erreur : choix d'activité invalide.")
        return

    facteur_activite = niveaux[choix]

    # Calcul BMR
    if sexe == "H":
        bmr = 10 * poids + 6.25 * taille - 5 * age + 5
    elif sexe == "F":
        bmr = 10 * poids + 6.25 * taille - 5 * age - 161
    else:
        print("Erreur : le sexe doit être H ou F.")
        return

    # Calcul TDEE
    tdee = bmr * facteur_activite

    print(f"\nBMR : {bmr:.2f} kcal/jour")
    print(f"TDEE (avec activité) : {tdee:.2f} kcal/jour")

    # Objectif
    print("\nQuel est votre objectif ?")
    print("1 - Sèche")
    print("2 - Maintenance")
    print("3 - Prise de masse")

    objectif = input("Votre choix (1-3) : ").strip()

    if objectif == "1":
        tdee_final = tdee * 0.85
    elif objectif == "2":
        tdee_final = tdee
    elif objectif == "3":
        tdee_final = tdee * 1.15
    else:
        print("Erreur : objectif invalide.")
        return

    print(f"\nTDEE ajusté selon votre objectif : {tdee_final:.2f} kcal/jour")


if __name__ == '__main__':
    calcul_bmr_tdee_objectif()
