"""
    Fichier contenant les boites contenant les lettres avec leur translation et couleur approprier pour le mini jeu de hangman
    Realiser par Cassey Martin et Jake Chagnon
"""
import pygame
from hang_constantes import etat_hangman
from hang_rectangle import rectangle
import random

class lettres:
    """
    Entrées: self
    Sorties: Aucune
    But: Créer un objet de lettres avec des boites(dynamiquement lorsque vert) en group sprite cases
    """
    def __init__(self):
        self.cases = pygame.sprite.Group() # Ne garanti pas l'ordre

        self.banque_mots = ["Condensateur", "Regulateur", "Multimetre", "Oscilloscope", "Impédance", "Amplificateur", "Microcontroleur", "Tension"]
        self.mot_choisi = random.choice(self.banque_mots) # choisit un mot au hasard parmis la liste

        self.espacement = 100

        self.y_rouge = 100
        self.rouges = [] # Utiliser cette liste pour garantir lordre
        self.x_decalage_rouge = 400
        self.erreurs_possible = 6 # Desire six lettres pour erreurs
        for i in range(self.erreurs_possible): 
            x = i*self.espacement + self.x_decalage_rouge
            emplacement = (x, self.y_rouge)
            rectangle_temporaire = rectangle(emplacement, (255, 0, 0)) # La couleur est rouge
            self.rouges.append(rectangle_temporaire)
            self.cases.add(rectangle_temporaire)

        self.y_vert = 600
        self.verts = [] # Utiliser cette liste pour garantir lordre
        self.x_decalage_vert = 100
        self.longeur_mot = len(self.mot_choisi)
        for i in range(self.longeur_mot): # Desire le nombre de case necessaire en fonction du mot
            x = i*self.espacement + self.x_decalage_vert
            emplacement = (x, self.y_vert)
            rectangle_temporaire = rectangle(emplacement, (0, 255, 0)) # La couleure est vert
            self.verts.append(rectangle_temporaire)
            self.cases.add(rectangle_temporaire)

    """
    Entrées: self
    Sorties: Letat du systeme apres la mise a jour
    But: Changer les parametres voulu des boites
    """
    def mettre_a_jour(self, etat, nouvelle_lettre):
        ajouter_vert = self.mettre_a_jour_vert(nouvelle_lettre)
        if not ajouter_vert and not nouvelle_lettre is None: # Mauvaise lettre
            self.mettre_a_jour_rouge(nouvelle_lettre)
            self.cases.update()
            if etat.value < self.erreurs_possible:
                return etat_hangman(etat.value + 1)
        else:
            self.cases.update()
        return etat
    """
    Entrées: self, ecran
    Sorties: rien
    But: Dessiner les cases avec leurs lettres sur lecran
    """
    def dessiner(self, ecran):
        self.cases.draw(ecran)
    
    """
    Entrées: self
    Sorties: Boolean(True ou False)
    But: Mettre a jour vert si la nouvelle lettre est dans mot choisi et non tapez, et savoir si des modifications vertes ont eu lieu
    """
    def mettre_a_jour_vert(self, nouvelle_lettre):
        modification = False
        for i in range(self.longeur_mot):
            lettre = self.mot_choisi[i]
            rectangle = self.verts[i]
            if lettre == nouvelle_lettre and rectangle.texte == "":# Si retape la meme lettre, lajoutera en erreur
                        rectangle.inserer_texte(nouvelle_lettre)
                        modification = True
        return modification
    
    """
    Entrées: self
    Sorties: Boolean(True ou False)
    But: Mettre a jour rouge
    """
    def mettre_a_jour_rouge(self, nouvelle_lettre):
        for rouge in self.rouges:
            if rouge.texte == "":
                rouge.inserer_texte(nouvelle_lettre)
                return




