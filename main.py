import pygame

WIN_WIDTH, WIN_HEIGHT = 780, 630
BG_COLOR = (0, 255, 0)

pygame.init()
pygame.display.set_caption('первая игра')
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

ran = True
while ran:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e. type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            ran = False

    screen.fill(BG_COLOR)
    pygame.display.update()