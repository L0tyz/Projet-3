
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Snakes and Ladders ULTRA MEGA DELUXE EDITION 2026")

BLANC = (255,255,255)
CLAIR = (170,170,170)
SOMBRE = (100,100,100)
BG = (60,25,60)

font = pygame.font.SysFont("Segoe UI", 40)

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((40, 40, 40))

        text = font.render("Chargement...", True, BLANC)
        screen.blit(text, (250, 350))

        pygame.display.update()

def start_menu():

    while True:

        screen.fill(BG)
        mouse = pygame.mouse.get_pos()

        play_button = pygame.Rect(300, 300, 140, 50)
        quit_button = pygame.Rect(300, 380, 140, 50)

        pygame.draw.rect(screen, CLAIR if play_button.collidepoint(mouse) else SOMBRE, play_button)
        pygame.draw.rect(screen, CLAIR if quit_button.collidepoint(mouse) else SOMBRE, quit_button)

        play_text = font.render("Jouer", True, BLANC)
        quit_text = font.render("Quitter", True, BLANC)

        screen.blit(play_text, (335, 305))
        screen.blit(quit_text, (335, 385))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_button.collidepoint(mouse):
                    game()

                if quit_button.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

start_menu()