# ============================
#   CONSTANTES
# ============================

ACTIVITY_LEVELS = {
    "1": ("Sédentaire", 1.2),
    "2": ("Léger (1-3 / semaine)", 1.375),
    "3": ("Modéré (3-5 / semaine)", 1.55),
    "4": ("Intense (6-7 / semaine)", 1.725),
    "5": ("Très intense (2 / jour)", 1.9),
}

OBJECTIVES = {
    "1": ("Sèche", 0.85),
    "2": ("Maintenance", 1.0),
    "3": ("Prise de masse", 1.15),
}


# ============================
#   VALIDATIONS
# ============================

def input_float(prompt, min_value=None, max_value=None):
    """Demande un nombre float valide dans une plage éventuelle."""
    while True:
        value = input(prompt).strip()
        try:
            number = float(value)
            if min_value is not None and number < min_value:
                print(f"Erreur : la valeur doit être ≥ {min_value}.")
                continue
            if max_value is not None and number > max_value:
                print(f"Erreur : la valeur doit être ≤ {max_value}.")
                continue
            return number
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")


def input_choice(prompt, valid_choices):
    """Demande un choix parmi une liste."""
    while True:
        value = input(prompt).strip()
        if value in valid_choices:
            return value
        print(f"Erreur : choix invalide. Options disponibles : {', '.join(valid_choices)}.")


def input_sexe(prompt):
    """Demande sexe en H ou F."""
    while True:
        value = input(prompt).strip().upper()
        if value in ("H", "F"):
            return value
        print("Erreur : entrez H ou F.")


# ============================
#   CALCULS
# ============================

def calcul_bmr(sexe, age, poids, taille):
    """Calcule le BMR selon Mifflin-St Jeor."""
    if sexe == "H":
        return 10 * poids + 6.25 * taille - 5 * age + 5
    else:
        return 10 * poids + 6.25 * taille - 5 * age - 161


def calcul_tdee(bmr, activity_factor):
    return bmr * activity_factor


def ajuster_objectif(tdee, objectif_factor):
    return tdee * objectif_factor


# ============================
#   MAIN WORKFLOW
# ============================

def main():
    print("=== Calcul PRO : BMR + TDEE + Objectif ===\n")

    # Inputs sécurisés
    sexe = input_sexe("Sexe (H/F) : ")
    age = input_float("Âge (années) : ", min_value=5, max_value=120)
    poids = input_float("Poids (kg) : ", min_value=20, max_value=500)
    taille = input_float("Taille (cm) : ", min_value=50, max_value=250)

    print("\nNiveau d'activité :")
    for key, (label, _) in ACTIVITY_LEVELS.items():
        print(f"{key} - {label}")

    activite = input_choice("\nVotre choix (1-5) : ", ACTIVITY_LEVELS.keys())
    _, activity_factor = ACTIVITY_LEVELS[activite]

    print("\nObjectif :")
    for key, (label, _) in OBJECTIVES.items():
        print(f"{key} - {label}")

    objectif = input_choice("\nVotre choix (1-3) : ", OBJECTIVES.keys())
    _, objectif_factor = OBJECTIVES[objectif]

    # Calculs
    bmr = calcul_bmr(sexe, age, poids, taille)
    tdee = calcul_tdee(bmr, activity_factor)
    tdee_final = ajuster_objectif(tdee, objectif_factor)

    # Résultats
    print("\n===== Résultats =====")
    print(f"BMR : {bmr:.2f} kcal/jour")
    print(f"TDEE (avant objectif) : {tdee:.2f} kcal/jour")
    print(f"TDEE ajusté (objectif) : {tdee_final:.2f} kcal/jour")


if __name__ == "__main__":
    main()
