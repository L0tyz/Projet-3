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
    Entrées: self, ecran, horloge, etat
    Sorties: Aucune
    But: Gérer le mini-jeu de hangman en fonction de son etat
    """
    def __init__(self, ecran, horloge):
        if ecran == None or horloge == None: # Mode test
            pygame.init() # Init pygame
            self.etat = "test"
            self.ecran = pygame.display.set_mode((hang_constantes.largeur_ecran, hang_constantes.hauteur_ecran)) # Initialization de l'écran
            self.horloge = pygame.time.Clock() # Horloge pour contrôler le temps
        else:
            self.ecran = ecran
            self.horloge = horloge
            self.etat = "vrai"
        pygame.display.set_caption(hang_constantes.entete) # Titre à l'affichage
        self.ecran.fill(hang_constantes.couleur_fond_ecran)
        
        self.temps_actuel = pygame.time.get_ticks() # Temps écoulé depuis le lancement du jeu en millisecondes
        self.running = True

        ### Initialization des objets ###
        self.obj_barbie = barbie()
        self.obj_ken = ken()

    def gerer_evenements(self):
        for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False

    def limiter_temps(self):
        temps_ecouler = (pygame.time.get_ticks() - self.temps_actuel)/1000 # Temps écoulé depuis le lancement du jeu en millisecondes
        if temps_ecouler >= 10:
            temps_ecouler = (pygame.time.get_ticks() - self.temps_actuel)/1000
            self.running = False  # Attendre 2 secondes avant de fermer le jeu

    def detection_collision(self):
        if pygame.sprite.spritecollideany(self.obj_barbie.hache, self.obj_ken.parts):
                print("Barbie a frapper Ken!")

        if pygame.sprite.groupcollide(self.obj_barbie.parts, self.obj_ken.parts, False, False):
            print("Collision détectée entre Barbie et Ken!")

    def update(self):
        self.obj_barbie.update()
        self.obj_ken.update()

    def draw(self):
        self.ecran.fill(hang_constantes.couleur_fond_ecran)

        self.obj_barbie.parts.draw(self.ecran)
        self.obj_ken.parts.draw(self.ecran)
        pygame.display.update()

    def run(self):
        while self.running:
            self.horloge.tick(60) # Limiter à 60 FPS
            self.limiter_temps()
            self.gerer_evenements()
            self.update()
            self.detection_collision()
            self.draw()
        if self.etat == "test":
            pygame.quit() # Clean exit

    #pygame.display.flip()
    #pygame.time.wait(2000)
    #ecran.blit(score_text, (10, 10))

hangman(None, None).run()    
