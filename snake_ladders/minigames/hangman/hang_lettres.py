"""
    Fichier contenant les boites qui contiennent les lettres avec leur translation et leur couleur approprier pour le mini jeu de hangman
    Realiser par Cassey Martin et Jake Chagnon
"""
import pygame
from hang_constantes import etat_hangman
from hang_rectangle import rectangle
import random

class lettres:
    """
    Entrées: self
    Sorties: Aucune (None par défaut, ce que python s'attend)
    But: Créer un objet de boites qui contiennent chacune une lettre et couleur grouper dans le group sprite cases
    """
    def __init__(self):
        self.cases = pygame.sprite.Group() # Ne garanti pas l'ordre

        self.banque_mots = ["Condensateur", "Regulateur", "Multimetre", "Oscilloscope", "Amplificateur", "Microcontroleur", "Tension"]
        self.mot_choisi = random.choice(self.banque_mots) # choisit un mot au hasard parmis la liste

        self.gagner = False
        self.espacement = 65

        self.y_rouge = 100
        self.rouges = [] # Utiliser cette liste pour garantir lordre
        self.x_decalage_rouge = 600
        self.erreurs_possible = len(etat_hangman) - 1 # Desire six lettres pour erreurs
        for i in range(self.erreurs_possible): 
            x = i*self.espacement + self.x_decalage_rouge
            emplacement = (x, self.y_rouge)
            rectangle_temporaire = rectangle(emplacement, (255, 179, 186)) # La couleur est rouge
            self.rouges.append(rectangle_temporaire)
            self.cases.add(rectangle_temporaire)

        self.y_vert = 600
        self.verts = [] # Utiliser cette liste pour garantir lordre
        self.x_decalage_vert = 15
        self.longeur_mot = len(self.mot_choisi)
        for i in range(self.longeur_mot): # Desire le nombre de case necessaire en fonction du mot
            x = i*self.espacement + self.x_decalage_vert
            emplacement = (x, self.y_vert)
            rectangle_temporaire = rectangle(emplacement, (186, 255, 201)) # La couleure est vert
            self.verts.append(rectangle_temporaire)
            self.cases.add(rectangle_temporaire)

    """
    Entrées: self
    Sorties: Letat du systeme apres la mise a jour(etat_hangman)
    But: Changer les parametres voulu des boites
    """
    def mettre_a_jour(self, etat, nouvelle_lettre):
        ### Verifier si doit ajouter vert ###
        ajouter_vert = False
        for i in range(self.longeur_mot):
            lettre = self.mot_choisi[i]
            rectangle = self.verts[i]
            if lettre.lower() == nouvelle_lettre and rectangle.texte == "":# Si retape la meme lettre, lajoutera en erreur
                rectangle.texte = str(nouvelle_lettre)
                ajouter_vert = True

        ### Si non, ajouter rouge si la lettre n'est pas None ###
        if not ajouter_vert and not nouvelle_lettre == None: # Mauvaise lettre
            for rouge in self.rouges:
                if rouge.texte == "":
                    rouge.texte = nouvelle_lettre # ajouter texte a la premiere case vide
                    self.cases.update()
                    if etat.value < self.erreurs_possible:
                        return etat_hangman(etat.value + 1) # Retourner le nouvelle etat

        ### Vérifier si gagne ###
        else:
            self.gagner = True
            for vert in self.verts:
                if vert.texte == "":
                    self.gagner = False
            self.cases.update()
        return etat # Retourner letat

    """
    Entrées: self, ecran
    Sorties: Listes des boites dessiner
    But: Dessiner les cases avec leurs lettres sur lecran
    """
    def dessiner(self, ecran):
        return self.cases.draw(ecran)