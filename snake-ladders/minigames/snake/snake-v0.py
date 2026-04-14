import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_radius = 10
player_color = "black"
score = 0

circle_radius = 20
circle_pos = pygame.Vector2(
    random.randint(0, screen.get_width()),
    random.randint(0, screen.get_height())
)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("grey")

   
    pygame.draw.circle(screen, player_color, player_pos, player_radius)
    pygame.draw.circle(screen, "red", circle_pos, circle_radius)
    pygame.display.set_caption(f"score: {score}")

    # movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # collision
    distance = player_pos.distance_to(circle_pos)
    if distance <= player_radius + circle_radius:
        
        circle_pos = pygame.Vector2(
            random.randint(0, screen.get_width()),
            random.randint(0, screen.get_height())
        )
        player_radius += 10
        score += 1
        
        
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
