"""
    Fichier contenant les membres de ken avec leur translation approprier pour le mini jeu de hangman
    Realiser par Cassey Martin et Jake Chagnon
"""
import pygame
class hang_ken:
    def __init__(self, bras_droit, bras_gauche, jambe_droite, jambe_gauche, tete, torse):
        self.bras_droit = bras_droit
        self.bras_gauche = bras_gauche
        self.jambe_droite = jambe_droite
        self.jambe_gauche = jambe_gauche
        self.tete = tete
        self.torse = torse
        
        
    @staticmethod
    def placer_ken():
        pass

    @classmethod 
    def swing_bras_droit_gauche():
        pass

    @classmethod
    def swing_bras_droit_droite():
        pass


    @staticmethod
    def load_image(nom_image):
        partie_image = pygame.image.load(nom_image).convert_alpha() # Enregistre(load) image dans la mémoire
        # .blit() montre sur l'écran
        # set_alpha() 255, pleinement visible
        # img = pygame.transform.scale(img, (64, 64))
        # img = pygame.transform.rotate(img, 45)
        #img = pygame.transform.flip(img, True, False)
        # frame = img.subsurface((x, y, width, height))
        # surface = pygame.Surface((width, height), pygame.SRCALPHA)
        # utiliser get_rect() pour la grandeur de limage
        # img = pygame.transform.smoothscale(img, (64, 64))
        # 0,0 a +x vers la droite et +y vers le bas
        # meme pour image puisque traiter comme rectangle peut importe la forme, mais tourne autour du centre de limage
        # every frame is rebuilt from scratch
