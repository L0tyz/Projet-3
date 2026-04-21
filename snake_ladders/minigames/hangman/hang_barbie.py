"""
    Fichier contenant les membres de ken avec leur translations appropriées pour le mini jeu de hangman
    Realisé par Cassey Martin et Jake Chagnon
"""
import pygame
from hang_constantes import hang_constantes
class barbie:
    """
    Entrées: self, hache, tronc, bras_droit, bras_gauche (Strings représentant l'emplacement des images dans les fichiers)
    Sorties: Aucune
    But: Créer la possibilité de faire un objet barbie
    """
    def __init__(self, hache, tronc, bras_droit, bras_gauche):
        try:
            # Enregistrer les images(loads) et ajuster sa grandeur
            self.hache = self.load_image(hache, hang_constantes.hache_scale_tuple)
            self.tronc = self.load_image(tronc, hang_constantes.barbie_scale)
            self.bras_droit = self.load_image(bras_droit, hang_constantes.barbie_scale)
            self.bras_gauche = self.load_image(bras_gauche, hang_constantes.barbie_scale)
        except FileNotFoundError:
            # Objet pas enregistrer en memoire
            # TODO: Gerer mieux
            self.hache = hache
            self.tronc = tronc
            self.bras_droit = bras_droit
            self.bras_gauche = bras_gauche

    """
    Entrées: self, image_voulu(nom de l'image), scale(tuple de la grandeur voulue)
    Sorties: image
    But: Créer une image uniformément et adéquatement(redimensionner avec bon parametres initiaux)
    """
    @classmethod
    def load_image(self, image_voulu, scale):
        image = pygame.image.load(image_voulu)
        image = image.convert_alpha()
        image = pygame.transform.smoothscale(image, scale)
        return image

    @staticmethod
    def placer_barbie():
        pass

    @staticmethod
    def load_image_two(nom_image):
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
