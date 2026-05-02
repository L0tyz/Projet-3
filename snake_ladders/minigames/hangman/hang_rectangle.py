"""
    Fichier contenant linterface sprite pour les membres de ken et barbie
    Realisé par Cassey Martin et Jake Chagnon
"""
import pygame

class rectangle(pygame.sprite.Sprite):

    """
    Entrées: self, hache, tronc, bras_droit, bras_gauche (Strings représentant l'emplacement des images dans les fichiers)
    Sorties: Aucune
    But: Créer la possibilité de créer une boite qui peut ajouter une lettre
    """
    def __init__(self, emplacement, couleur):
        super().__init__()

        self.image = pygame.Surface((60, 40)) # Sprite sattend a une image
        self.couleur = couleur
        self.image.fill(self.couleur)

        self.rect = self.image.get_rect(topleft=emplacement)

        self.texte = ""
        self.font = pygame.font.Font(None, 20)

        self.surface_texte = self.font.render(self.texte, True, (0, 0, 0))

    """
    Entrées: self
    Sorties: rien
    But: Mettre a jour les parametres voulu de la partie
    """
    def update(self):
        #may need to color again
        self.image.fill(self.couleur)
        pygame.draw.rect(self.image, self.couleur, self.image.get_rect())
        
        self.surface_texte = self.font.render(self.texte, True, (0, 0, 0))

        text_rect = self.surface_texte.get_rect(center=self.image.get_rect().center)
        self.image.blit(self.surface_texte, text_rect)
        #self.image.blit(self.image, self.rect)
    """
    Entrées: self
    Sorties: rien
    But: Mettre a jour les parametres voulu de la partie
    """
    def inserer_texte(self, nouveau_texte):
        self.texte = str(nouveau_texte)
        self.update()