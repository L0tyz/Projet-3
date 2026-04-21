# TODO: Dump
import cv2
import os
import hang_constantes

def remove_white_borders(image_path):
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

#remove_white_borders(hang_constantes.barbie_hache)
#remove_white_borders(hang_constantes.barbie_marteau)
#remove_white_borders(hang_constantes.barbie_tt_seule)
##remove_white_borders(hang_constantes.hammer)
#r#emove_white_borders(hang_constantes.ken_bras_droit)
#remove_white_borders(hang_constantes.ken_bras_gauche)
#remove_white_borders(hang_constantes.ken_jambe_droite)
#remove_white_borders(hang_constantes.ken_torse)
#remove_white_borders(hang_constantes.ken_jambe_gauche)
#remove_white_borders(hang_constantes.ken_tete)
#remove_white_borders(hang_constantes.barbie_bras_droit)
#remove_white_borders(hang_constantes.barbie_bras_gauche)
#remove_white_borders(hang_constantes.barbie_tronc)