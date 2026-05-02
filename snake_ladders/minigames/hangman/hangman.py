"""    
    Realisé par Cassey Martin et Jake Chagnon
    But: Fichier principale du jeu hangman
"""
import pygame
from hang_constantes import hang_constantes
from hang_constantes import etat_hangman
from hang_barbie import barbie
from hang_ken import ken
from hang_lettres import lettres

class hangman:
    """
    Entrées: self
    Sorties: Aucune (None par défaut, ce que python s'attend)
    But: Initialiser l'objet hangman pour gérer ce jeu
    """
    def __init__(self):
        pygame.init() # Init pygame
        self.ecran = pygame.display.set_mode((hang_constantes.largeur_ecran, hang_constantes.hauteur_ecran)) # Initialization de l'écran
        self.horloge = pygame.time.Clock() # Horloge pour contrôler le temps

        pygame.display.set_caption(hang_constantes.entete) # Titre à l'affichage

        pygame.font.init() # Initialization des lettres

        self.ecran.fill(hang_constantes.couleur_fond_ecran)

        self.running = True
        self.hang_etat = etat_hangman.AUCUN_ECHEC

        self.nom_cle = None
        self.booster = 1

        ### Initialization des objets ###
        self.obj_barbie = barbie()
        self.obj_ken = ken()
        self.obj_lettres = lettres()

    """
    Entrées: self
    Sorties: Le nombre de points en fonction du succes lors du jeu
    But: Demarrer et executer le mini-jeu de hangman
    """
    def run(self):
        while self.running:
            self.horloge.tick(60) # Limiter à 60 FPS

            ### Gerer evenement ###
            self.nom_cle = None # Remettre nom_cle a None
            for e in pygame.event.get():
                    peut_sauvegarder_cle = (
                        e.type == pygame.KEYDOWN and # Verifier si cle a ete pesser
                        not self.hang_etat == etat_hangman.SIX_ERREURS and # Rend impossible denregistrer reponse lorsque six erreurs
                        not self.obj_barbie.aller # Rend impossible denregistrer reponse avant que barbie enleve au moins une partie de ken
                    ) 
                    if peut_sauvegarder_cle:
                        self.nom_cle = pygame.key.name(e.key).lower() # Mettre nom_cle a sa valeur actuelle
                        print(self.nom_cle)
                    if e.type == pygame.QUIT:
                        self.running = False

            ### Mettre a jour les situations dobjets ###
            self.hang_etat = self.obj_lettres.mettre_a_jour(self.hang_etat, self.nom_cle) # Mettre a jour letat
            partie_frapper = pygame.sprite.spritecollideany(self.obj_barbie.hache, self.obj_ken.parts)
            self.running = self.obj_barbie.mettre_a_jour(self.hang_etat) # Mettre a jour le statut du jeu
            self.booster = self.obj_ken.mettre_a_jour(self.hang_etat, partie_frapper) # Mettre a jour le booster

            ### Dessiner ###
            self.ecran.fill(hang_constantes.couleur_fond_ecran) # Reinitialiser fond d'ecran
            self.obj_barbie.dessiner(self.ecran)
            self.obj_ken.dessiner(self.ecran)   
            self.obj_lettres.dessiner(self.ecran)

            self.running = self.running and not self.obj_lettres.gagner # Arreter jeu si joueur gagne: (True and not True)= False
            pygame.display.update()

        return 100 * self.booster # si reste aucune partie de ken sera 0

print(hangman().run())

