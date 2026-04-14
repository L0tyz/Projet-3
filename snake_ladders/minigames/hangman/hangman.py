import pygame
from hang_constantes import hang_constantes
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
        while running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
            temps_ecouler = (pygame.time.get_ticks() - temps_actuel)/1000 # Temps écoulé depuis le lancement du jeu en millisecondes
            if temps_ecouler >= 10:
                temps_ecouler = (pygame.time.get_ticks() - temps_actuel)/1000
                running = False  # Attendre 2 secondes avant de fermer le jeu
        pygame.quit() # Clean exit

    #pygame.display.flip()
    #pygame.time.wait(2000)
    #ecran.blit(score_text, (10, 10))

hangman.hangman()    
