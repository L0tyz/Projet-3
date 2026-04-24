class Colors:
	couleur_fenetre = (0, 0, 0)
	couleur_lblock = (0, 255, 0)
	couleur_jblock = (255, 0, 0)
	couleur_iblock = (255, 255, 255)
	couleur_oblock = (255, 255, 255)
	couleur_sblock = (0, 255, 255)
	couleur_tblock = (255, 255, 255)
	couleur_zblock = (0, 0, 255)
	couleur_texte = (255, 255, 255)
	couleur_fond = (0, 0, 0)
	couleur_carre = (59, 85, 162)

	@classmethod
	def get_cell_colors(cls):
		return [cls.couleur_fenetre, cls.couleur_lblock, cls.couleur_jblock, cls.couleur_iblock, cls.couleur_oblock, cls.couleur_sblock, cls.couleur_tblock, cls.couleur_zblock]