class Colors:    
    
    gris_foncer = (26, 31, 40)
    vert = (47, 230, 23)
    rouge = (232, 18, 18)
    orange = (226, 116, 17)
    jaune = (237, 234, 4)
    mauve = (166, 0, 247)
    cyan = (21, 204, 209)
    bleu = (13, 64, 216)

#defenir une methode qui peut etre appeler sur une class
#au lieu de l'etre a un instant dans la classe 
    @classmethod
    def get_cell_colors(cls):
        return [cls.gris_foncer, cls.vert, cls.rouge, cls.orange, cls.jaune, cls.mauve, cls.cyan, cls.bleu]