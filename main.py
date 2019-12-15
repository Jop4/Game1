import pygame

level = [
    '--------------------------',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '--------------------------'
]

WIN_WIDTH, WIN_HEIGHT = 780, 630
BG_COLOR = (192, 192, 192)
BRICK_WIDTH = BRICK_HEIGHT = 30
BRICK_COLOR = (0, 128, 0)
FPS = 60
clock = pygame.time.Clock()
x1, y1 = WIN_WIDTH // 2, WIN_WIDTH // 2
PLAYER_SIZE = 50, 50

pygame.init()
pygame.display.set_caption('первая игра')
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

player = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
 # brick.fill(BRICK_COLOR)

ran = True
while ran:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e. type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            ran = False

    screen.fill(BG_COLOR)

    x = 0
    y = 0
    for row in level:
        for col in row:
            if col == '-':
                screen.blit(player, (x1, y1))
                brick = pygame.draw.rect(screen, BRICK_COLOR, [x, y, BRICK_WIDTH, BRICK_HEIGHT])
                pygame.draw.rect(screen,(100, 0, 0), [x, y, BRICK_WIDTH, BRICK_HEIGHT], 2)
            x += BRICK_WIDTH
        y += BRICK_HEIGHT
        x = 0

    pygame.display.set_caption(f' FPS: {round(clock.get_fps(), 1)}')
    pygame.display.update()
    clock.tick(FPS)
