# Hangman

## Description

Mini jeu dont le but est de trouver le mot complet fourni aléatoirement. Afin de le deviner, il faut taper des lettres. Si l'utilisateur atteint 6 mauvaises devinette de lettre, il a perdu. S'il devine le mot en moins de six devinette il a gagné.

---
## Requis
1. Dans le terminal de VS code exécuter la commande: `pip install pygame`
---
## Organisation des fichiers
1. `hangman.md`: Introduction
2. `hangman.py`: Contrôle d'affichage
3. `hang_lettres.py`: Barre rouge et verte qui represente respectivement les erreurs commise et le mot dans son ordre
4. `hang_ken.py`: Affichage du personnage a abattre
5. `hang_barbie.py`: Affichage du personnage qui abat
6. `hang_partie.py`: Objet image
7. `hang_rectangle.py`: Objet rectangle
8. `hang_sang.py`: Physique du sang
9. `hangman\assets`: Images utiliser
10. `hang_constantes.py`: Constantes utiliser pour hangman

---
## Methode a mettre dans main
`hangman(ecran_du_jeu, horloge).run()`
-`hangman(ecran_du_jeu, horloge)`: Lobjet
-`run()`: La methode
 