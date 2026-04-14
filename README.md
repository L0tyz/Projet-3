# BASE DU PROJET 3 - SNAKES AND LADDERS

## 🎮 Guide d'Installation pygame-ce : 

** Bienvenue ! **

```pygame-ce``` est la version "Community Edition", une version améliorée, plus rapide et plus régulièrement mise à jour que la bibliothèque originale. Cette version de pygame sera necessaire📋

https://github.com/pygame-community/pygame-ce

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir Python installé sur ton ordinateur. Version minimale : Python 3.10 ou supérieur.
```python -v```

## 🚀 Étape 1 : Installation 


Pour installer la bibliothèque, utilise l'outil pip (le gestionnaire de paquets de Python). Copiez et collez la commande suivante dans votre terminal: ``` pip install pygame-ce ```


[!IMPORTANT ]Cas particuliers: Si la commande pip ne fonctionne pas, essayez: ``` pip3 install pygame-ce ``` ou```  python -m pip install pygame-ce```.
Attention : Si vous avez déjà installé l'ancien pygame (standard), il est fortement recommandé de le désinstaller d'abord avec ```pip uninstall pygame``` pour éviter les conflits.

## ✅ Étape 2 : Vérifier que tout fonctionne

Pour tester si l'installation a réussi, crée un nouveau fichier nommé ``` test_pygame.py```:
``` 
# Initialisation de tous les modules
pygame.init()

# Création d'une fenêtre simple
ecran = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Ma première fenêtre pygame-ce !")

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

    ecran.fill((45, 140, 245)) # Un beau bleu
    pygame.display.flip()

pygame.quit()
``` 
Lance le script. Si une fenêtre bleue apparaît, vous etes prêt à coder !


## 📚 Ressources et Documentation

Voici les liens essentiels pour vous aidez:

###📖 Documentation Officielle

Documentation de pygame-ce : Le guide complet de toutes les fonctions https://pyga.me/docs/ 
