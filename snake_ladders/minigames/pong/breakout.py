import pygame

pygame.init()

ecran = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

vitesse = 300
possition_balle_x = 640
possition_balle_y = 360
rayon_balle = 20

joueur = pygame.Rect(640, 680, 150, 20)


mur = pygame.Rect(0, 0, 78, 25)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    ecran.fill((0, 0, 0))

   
    joueur.clamp_ip(ecran.get_rect())
    pygame.draw.rect(ecran, ("white"), joueur)

                  # debut, fin, pas
    for i in range(1, 1280, 80):
        mur.x = i
        pygame.draw.rect(ecran, ("grey"), mur)
        for j in range(2, 100, 27):
            mur.y = j
            pygame.draw.rect(ecran, ("grey"), mur)
    
    touches = pygame.key.get_pressed()
    if touches[pygame.K_a]:
        joueur.x -= vitesse * dt / 1000
    if touches[pygame.K_d]:
        joueur.x += vitesse * dt / 1000

    

    pygame.display.flip()
    dt = clock.tick(60)
