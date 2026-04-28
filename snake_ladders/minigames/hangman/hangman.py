"""    
    Realisé par Cassey Martin et Jake Chagnon
"""
import pygame
from hang_constantes import hang_constantes
from hang_constantes import etat_hangman
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
        self.erreurs = 0
        self.running = True

        ### Initialization des objets ###
        self.obj_barbie = barbie()
        self.obj_ken = ken()

    """
    Entrées: self
    Sorties: Aucune
    But: Gérer le mini-jeu de hangman avec pygame
    """
    def gerer_evenements(self):
        for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False

    # TODO:MAYBE DUMP
    def limiter_temps(self):
        temps_ecouler = (pygame.time.get_ticks() - self.temps_actuel)/1000 # Temps écoulé depuis le lancement du jeu en millisecondes
        if temps_ecouler >= 10:
            temps_ecouler = (pygame.time.get_ticks() - self.temps_actuel)/1000
            self.running = False  # Attendre 2 secondes avant de fermer le jeu

    """
    Entrées: self
    Sorties: Aucune
    But: Ajouter une erreur lorsque lutilisateur nappuie pas sur la bonne touche(pour changer letat des objets)
    """
    def ajouter_erreur(self):
        if pygame.key.get_just_pressed()[pygame.K_b] and self.erreurs < 6: # Limiter les erreurs à 6
            self.erreurs += 1
    """
    Entrées: self
    Sorties: Aucune
    But: Mettre a jour les valeurs pour quils soient celle a afficher a lecran en prochain
    """
    def mettre_a_jour(self):
        etat = etat_hangman(self.erreurs) 
        partie_frapper = pygame.sprite.spritecollideany(self.obj_barbie.hache, self.obj_ken.parts)
        self.obj_barbie.mettre_a_jour(etat)
        self.obj_ken.mettre_a_jour(etat, partie_frapper)
    """
    Entrées: self
    Sorties: Aucune
    But: Rafraichir lecran et dessiner les objets
    """
    def dessiner(self):
        self.ecran.fill(hang_constantes.couleur_fond_ecran)
        self.obj_barbie.dessiner(self.ecran)
        self.obj_ken.dessiner(self.ecran)   
    """
    Entrées: self
    Sorties: Aucune
    But: Demarrer et executer le mini-jeu de hangman
    """
    def run(self):
        #pygame.event.set_grab(True) # Assuer que lattention est sur le jeu pour assurer de detecter le tapes des touches
        while self.running:
            self.horloge.tick(60) # Limiter à 60 FPS
            self.ajouter_erreur()
            #self.limiter_temps()
            if self.erreurs == 7: # TODO:Exit cleaner
                self.running = False # TODO: Rendre impossible de changer detat avant quanimation soit terminer(obj_barbie.retour = False)
            self.gerer_evenements()
            self.mettre_a_jour()
            self.dessiner()
            pygame.display.update()
            
        if self.etat == "test":
            pygame.quit() # Clean exit

    #pygame.display.flip()
    #pygame.time.wait(2000)
    #ecran.blit(score_text, (10, 10))

hangman(None, None).run()    
