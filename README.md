# Projet Snake and ladders — Version ultime

Ce jeu consiste d'un jeu principal, avec une amélioration : des cases mini-jeu pour vous aider ou vous nuire dans votre progrès! Voici les mini-jeux, choisis aléatoirement par le jeu, que vous devez conquérir : 
- Color Conquest — conquête de couleurs (mini-jeu de capture par palette)
- Hangman — jeu du bonhomme pendu
- Snake — serpent classique
- Tetris — empilement de blocs
- TicTacToe — un classique!

---
## Mise en place rapide
Pré-requis : Python 3.10+ et pip.

Il faudra installer Pygame (recommandé : `pygame-ce`) :
```
powershell
pip install pygame-ce
````

Si `pip` ne fonctionne pas : `pip3 install pygame-ce` ou `python -m pip install pygame-ce`.

Si vous avez une ancienne installation de `pygame`, désinstallez-la d'abord :
```powershell
pip uninstall pygame
```
puis réessayez l'installation de `pygame-ce`.

---

## Règles 

### Jeu principal

### Color conquest

- Grille 10×10 initialisée aléatoirement parmi 5 couleurs : rose, orange, rouge, jaune et violet.
- Cliquer une couleur applique immédiatement cette couleur à la zone connectée contenant la case en bas à gauche (algorithme de flood‑fill).
- Nombre limité de sélections : si la limite est dépassée, le jeu est perdu!

### Hangman

- Le joueur doit deviner un mot lettre par lettre.
- À chaque lettre incorrecte, une partie du bonhomme est dessinée ; après un nombre limité d'erreurs, le joueur perd.
- Le joueur gagne s'il devine toutes les lettres avant d'atteindre le nombre maximum d'erreurs.

### Snake

- Le joueur contrôle un serpent qui se déplace sur une grille.
- Le but est de manger des objets (nourriture) qui allongent le serpent et rapportent des points.
- Le joueur perds si le serpent touche les murs ou se mord la queue (collision avec lui‑même), et il gagne s'il fait assez de points.

### Tetris
Petit résumé :

- Des pièces de différentes formes tombent progressivement depuis le haut de l'écran.
- Le joueur peut déplacer et faire pivoter les pièces pour former des lignes horizontales complètes.
- Lorsqu'une ligne est remplie, elle disparaît et rapporte des points. 
- Pour gagner, il faut que le joueur fasse au moins 800 points avant de mourir, sinon le joueur perd.

### TicTacToe

- Deux joueurs s'affrontent sur une grille 3×3 en choisissant alternativement X ou O.
- Le premier joueur qui aligne trois symboles (horizontalement, verticalement ou en diagonale) gagne.
- Si la grille est remplie sans alignement, la partie est nulle.

### Pong (multijoueur)

- Deux joueurs contrôlent chacun une raquette verticale de part et d'autre de l'écran.
- Une balle rebondit et chaque joueur tente de l'envoyer hors de portée de l'adversaire.
- Le joueur marque un point quand l'adversaire manque la balle; le premier à atteindre le score cible gagne.
  
---

## Arborescence importante

```
main.py
README.md
snake_ladders/
    minigames/
        colorconquest/
            colorconquest.py
        hangman/
            hangman.py
        snake/
            snake.py
        tetris/
            tetris.py
        tictactoe/
            tictactoe.py
```

---

## Choses à améliorer

| # | Tâche | Statut | Description courte |
|---:|:------|:------:|:------------------|
| 1 | Vérifier le minijeu Color Conquest | ✅ Complété | Lancer et tester palette, flood‑fill et messages FR |
| 2 | Menu principal | ✅ Complété | Interface pour lancer chaque mini‑jeu depuis le plateau |
| 3 | Polissage UI | ⌛ En attente | Améliorer police, responsive et animations |
| 4 | Modes de jeux | ⌛ En attente | Ajouter des modes de jeux et des options de difficulté |

---

## Besoin d'aide ?

- La fenêtre Pygame ne s'ouvre pas : lancez depuis un terminal et lisez les messages d'erreur.
- Problèmes d'installation : vérifiez la version de Python et l'environnement virtuel utilisé.

---

