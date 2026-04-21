# Hangman

## Description

Mini jeu dont le but est de trouver le mot complet fourni aléatoirement. Afin de le deviner, il faut taper des lettres. Si l'utilisateur atteint 6 mauvaises devinette de lettre, il a perdu. S'il devinne le mot en moins de six devinette il a gangné.

---
## Requis
1. Dans le terminal de VS code exécuter la commande: `pip install pygame`
---
## Organisation des fichiers
1. `hangman.md`: Introduction
2. `hangman.py`: Contrôle d'affichage et de logique
3. `hang_logique.py`: Logique
4. `hang_lettres.py`: Barre que les lettres tapez apparaît(Avec fonts au besoin)
5. `hang_ken.py`: Affichage du personnage a abattre
6. `hang_outils.py`: Outils utilisé pour abattre
7. `hang_sang.py`: Physique du sang
8. `hangman\assets`: Images utiliser

---
## Buts créatifs
   - Simulation physique plus ou moins réaliste de sang lors des echecs(Abattrement)