"""
    Fichier contenant les membres de ken avec leur translations appropriées pour le mini jeu de hangman
    Realisé par Cassey Martin et Jake Chagnon
"""
import pygame
from hang_constantes import hang_constantes
class barbie:
    """
    Entrées: outils(liste des noms des images des outils de barbie), barbie(nom de l'image)
    Sorties: Aucune
    But: Créer la possibilité de faire un objet barbie
    """
    def __init__(self, hache, marteau, barbie):
        try:
            # Enregistrer les images(loads) et ajuster sa grandeur
            self.barbie = pygame.transform.smoothscale(pygame.image.load(barbie).convert_alpha(), (hang_constantes.barbie_largeur, hang_constantes.barbie_grandeur))
            self.hache = pygame.transform.smoothscale(pygame.image.load(hache).convert_alpha(), (hang_constantes.hache_scale, hang_constantes.hache_scale))
            self.marteau = pygame.transform.smoothscale(pygame.image.load(marteau).convert_alpha(), (hang_constantes.hammer_scale, hang_constantes.hammer_scale))
        except FileNotFoundError:
            # Objet pas enregistrer en memoire
            # TODO: Gerer mieux
            self.barbie = barbie
            self.hache = hache
            self.marteau = marteau

    @staticmethod
    def placer_barbie():
        pass

    @staticmethod
    def load_image(nom_image):
        partie_image = pygame.image.load(nom_image).convert_alpha() 
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
