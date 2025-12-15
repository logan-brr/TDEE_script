#Calcul de la dépense énergétique quotidienne totale (TDEE)

Ce script Python a été rédigé avec l'aide de ChatGPT pour un entraînement à la programmation. Il constitue une version plus professionnelle de la première version du script.

## Description

Le script calcule la dépense énergétique quotidienne totale d'un individu selon la formule de Mifflin-St Jeor. Il demande à l'utilisateur de saisir :

- Son sexe
- Son âge
- Son poids
- Sa taille
- Son niveau d'activité (nombre de séances de sport par semaine)
- Son objectif (sèche, maintenance, prise de masse)

##Installation / Prérequis

- Python 3.14.0
- Téléchargez le fichier tdee.py
- Lancez-le depuis votre terminal ou IDE

##Améliorations du script initial

- Structure claire et lisible : sections distinctes pour constantes, inputs, calculs et workflow principal.
- Fonctions pures pour les calculs : facilite les tests unitaires.
- Centralisation des constantes : dictionnaires ACTIVITY_LEVELS et OBJECTIVES pour une maintenance plus facile (principe DRY).
- Robustesse :
  - Boucles while True et continue pour validation des entrées utilisateur
  - Gestion des erreurs via try/except et validation par plages (âge, taille, poids)
  - Le script est importable comme module et peut être utilisé seul ou intégré dans d'autres projets.

##Tests

Le fichier de test contient des tests unitaires pour :
- calcul_bmr : métabolisme de base
- calcul_tdee : besoins en fonction de l'activité physique
- ajuster_objectif : ajustement selon l'objectif

Licence

MIT