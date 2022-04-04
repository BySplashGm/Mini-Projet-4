import pygame
import sys

# Initialisation du module pygame
pygame.init()

# Génération de la fenêtre
screen = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("Mini Projet 4")

Clock = pygame.time.Clock()

running = True

background = pygame.image.load('office.png')

j = 0
i = 360

while running:

    bg_rect = background.get_rect()
    bg_rect.center = (j, i)
    screen.blit(background, bg_rect)

    Clock.tick()
    pygame.display.set_caption("MP4 - " + str(int(Clock.get_fps())) + "FPS")
    pygame.display.update()  # Actualiser l'écran
    pygame.display.flip()  # Actualiser l'écran
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        mx, my = pygame.mouse.get_pos()
        if mx >= 600:
            j = 1600-mx
        elif mx <= 1000:
            j = 1600-mx
        else:
            j = 800

