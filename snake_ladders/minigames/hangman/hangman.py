"""    
    Realisé par Cassey Martin et Jake Chagnon
"""
import pygame
from hang_constantes import hang_constantes
from hang_barbie import barbie
from hang_ken import ken
#from hang_logique import hang_logique

class hangman:
    """
    Entrées: Aucune
    Sorties: Aucune
    But: Gérer le mini-jeu de hangman
    """
    @staticmethod
    def hangman():
        pygame.init() # Init pygame
        ecran = pygame.display.set_mode((hang_constantes.largeur_ecran, hang_constantes.hauteur_ecran)) # Initialization de l'écran
        pygame.display.set_caption(hang_constantes.entete) # Titre à l'affichage

        ecran.fill(hang_constantes.rgb_noir)

        clock = pygame.time.Clock() # Horloge pour contrôler le temps
        clock.tick(60) # Limiter à 60 FPS
        temps_actuel = pygame.time.get_ticks() # Temps écoulé depuis le lancement du jeu en millisecondes
        running = True

        ### Initialization des objets ###
        obj_barbie = barbie(hang_constantes.hache, hang_constantes.barbie_tronc,hang_constantes.barbie_bras_gauche, hang_constantes.barbie_bras_droit)
        obj_ken = ken(hang_constantes.ken_bras_droit, hang_constantes.ken_bras_gauche, hang_constantes.ken_jambe_droite, hang_constantes.ken_jambe_gauche, hang_constantes.ken_tete, hang_constantes.ken_torse)

        while running:
            #ecran.blit(pygame.image.load(hang_constantes.barbie_tt_seule), (100, 100), (1, 1)) #, ecran.get_rect(center=(hang_constantes.largeur_ecran//2, hang_constantes.hauteur_ecran//2))) # Afficher la barbie au centre de l'écran
            try:
                # when obj is a string
                for attr, value in vars(obj_barbie).items():
                    print(attr)
                    ecran.blit(value, (hang_constantes.largeur_ecran//2 - 50, hang_constantes.hauteur_ecran//2 - 50)) #, ecran.get_rect(center=(hang_constantes.largeur_ecran//2, hang_constantes.hauteur_ecran//2))) # Afficher la barbie au centre de l'écran
                for attr, value in vars(obj_ken).items():
                    print(attr)
                    ecran.blit(value, (hang_constantes.largeur_ecran//2 + 100, hang_constantes.hauteur_ecran//2 + 100))
            except Exception as e:
                print(f"Error loading image: {e}")
                pass

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
            temps_ecouler = (pygame.time.get_ticks() - temps_actuel)/1000 # Temps écoulé depuis le lancement du jeu en millisecondes
            if temps_ecouler >= 10:
                temps_ecouler = (pygame.time.get_ticks() - temps_actuel)/1000
                running = False  # Attendre 2 secondes avant de fermer le jeu
            pygame.display.update() # Mettre à jour l'affichage
        pygame.quit() # Clean exit

    #pygame.display.flip()
    #pygame.time.wait(2000)
    #ecran.blit(score_text, (10, 10))

hangman.hangman()    
