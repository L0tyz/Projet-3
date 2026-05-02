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
        pygame.font.Font(None, 20)

        self.ecran.fill(hang_constantes.couleur_fond_ecran)

        self.running = True
        self.hang_etat = etat_hangman.AUCUN_ECHEC

        self.nom_cle = None
        ### Initialization des objets ###
        self.obj_barbie = barbie()
        self.obj_ken = ken()
        self.obj_lettres = lettres()

    """
    Entrées: self
    Sorties: Aucune
    But: Mettre a jour les valeurs pour quils soient celle a afficher a lecran en prochain
    """
    def mettre_a_jour(self):
        self.hang_etat = self.obj_lettres.mettre_a_jour(self.hang_etat, self.nom_cle)
        partie_frapper = pygame.sprite.spritecollideany(self.obj_barbie.hache, self.obj_ken.parts)
        self.obj_barbie.mettre_a_jour(self.hang_etat)
        self.obj_ken.mettre_a_jour(self.hang_etat, partie_frapper)
    """
    Entrées: self
    Sorties: Aucune
    But: Rafraichir lecran et dessiner les objets
    """
    def dessiner(self):
        self.ecran.fill(hang_constantes.couleur_fond_ecran)
        self.obj_barbie.dessiner(self.ecran)
        self.obj_ken.dessiner(self.ecran)   
        self.obj_lettres.dessiner(self.ecran)
    """
    Entrées: self
    Sorties: Aucune
    But: Demarrer et executer le mini-jeu de hangman
    """
    def run(self):
        while self.running:
            self.horloge.tick(60) # Limiter à 60 FPS
            # TODO: Rendre impossible de changer detat avant quanimation soit terminer(obj_barbie.retour = False)
            if self.obj_barbie.end:
                self.running = False 

            self.nom_cle = None # Remettre nom_cle a None
            for e in pygame.event.get(): # Gerer evenement
                    if e.type == pygame.KEYDOWN:
                        self.nom_cle = pygame.key.name(e.key) # Mettre nom_cle a sa valeur actuelle
                    if e.type == pygame.QUIT:
                        self.running = False
            self.mettre_a_jour()
            self.dessiner()
            if self.obj_lettres.gagner:
                self.running = False
            pygame.display.update()
        #pygame.quit() # Clean exit(not for main)

hangman().run()    
