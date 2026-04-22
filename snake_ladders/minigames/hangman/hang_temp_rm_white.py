# TODO: Dump
import cv2
import os
from hang_constantes import hang_constantes
import pygame

pygame.init()
ecran = pygame.display.set_mode((hang_constantes.largeur_ecran, hang_constantes.hauteur_ecran)) # Initialization de l'écran
horloge = pygame.time.Clock() # Horloge pour contrôler le temps

def load_clean_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold to isolate non-white areas (values < 240 considered content)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    # Find coordinates of all non-zero (content) pixels
    coords = cv2.findNonZero(thresh)
    x, y, w, h = cv2.boundingRect(coords)

    # Crop the original image
    cropped_img = img[y:y+h, x:x+w]
    cv2.imwrite(image_path, cropped_img)

def remove_white_borders(path):
    # 2. Otherwise process it
    img = pygame.image.load(path).convert_alpha()
    img = enlever_blanc(img)

    # 3. Save result for next time
    pygame.image.save(img, path)
    return img

def enlever_blanc(image):
        largeur, grandeur = image.get_size()
        threshold = hang_constantes.blanc_tolerance
        for x in range(largeur):
            for y in range(grandeur):
                r, g, b, a = image.get_at((x,y))
                if r > threshold and g > threshold and b > threshold:
                    image.set_at((x, y), hang_constantes.couleur_fond_ecran)
        return image

remove_white_borders(hang_constantes.barbie_hache)
remove_white_borders(hang_constantes.barbie_marteau)
remove_white_borders(hang_constantes.barbie_tt_seule)
remove_white_borders(hang_constantes.hammer)
remove_white_borders(hang_constantes.ken_bras_droit)
remove_white_borders(hang_constantes.ken_bras_gauche)
remove_white_borders(hang_constantes.ken_jambe_droite)
remove_white_borders(hang_constantes.ken_torse)
remove_white_borders(hang_constantes.ken_jambe_gauche)
remove_white_borders(hang_constantes.ken_tete)
remove_white_borders(hang_constantes.barbie_bras_droit)
remove_white_borders(hang_constantes.barbie_bras_gauche)
remove_white_borders(hang_constantes.barbie_tronc)
pygame.quit()