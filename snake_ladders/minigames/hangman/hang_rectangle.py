"""
    Fichier contenant linterface sprite pour les lettres
    Realisé par Cassey Martin et Jake Chagnon
"""
import pygame

class rectangle(pygame.sprite.Sprite):

    """
    Entrées: self, emplacement, couleur
    Sorties: Aucune (None par défaut, ce que python s'attend)
    But: Créer la possibilité de créer une boite qui peut ajouter une lettre avec sa couleur
    """
    def __init__(self, emplacement, couleur):
        super().__init__()

        self.image = pygame.Surface((60, 40)) # Sprite sattend a une image
        self.couleur = couleur
        self.image.fill(self.couleur)

        self.rect = self.image.get_rect(topleft=emplacement)

        self.texte = ""
        self.font = pygame.font.Font(None, 20)
        self.texte_color = (0, 0, 0)
        self.surface_texte = self.font.render(self.texte, True, self.texte_color)

    """
    Entrées: self
    Sorties: Aucune (Mauvaise pratique avec l'interface puisque servirait à rien dans le programme)
    But: Mettre a jour les parametres voulu de la partie
    NOTE: Appeler automatiquement par Sprite(Elle DOIT s'appeler update())
    """
    def update(self):
        self.image.fill(self.couleur) # Eviter que les lettres grossisent(ghosting)

        self.surface_texte = self.font.render(self.texte, True, (0, 0, 0)) # Surface du texte
        text_rect = self.surface_texte.get_rect(center=self.image.get_rect().center) # Rectangle du texte
        self.image.blit(self.surface_texte, text_rect) # Dessiner lettre