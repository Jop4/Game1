import pygame

level = [
    '------------------------------------------------------------------------------------------',
    '-                                                                                        -',
    '-  --- -    -  - -  -   ---  - - - -                                          ---        -',
    '-   -  ---  -  --  - -  - -   -  ---                    -----                 ---        -',
    '-   -  ---  -  - - - -  ---   -  - -                       ---                ---        -',
    '-                                                      ------                            -',
    '-                                                                                        -',
    '-          ----                                                                          -',
    '-           ---                 -   -                                                    -',
    '-                                                -                        ---            -',
    '-                              -     -          ---                       ---            -',
    '-                               -----            -                                       -',
    '-                      ---                                                               -',
    '-                      ---                                       ---                     -',
    '-                                                                 --            ---      -',
    '-                                                                  --            ---     -',
    '-            --                   ---           ----                           ----      -',
    '-           ---                   ---            --                                      -',
    '-                                                                                        -',
    '-                                                                                        -',
    '------------------------------------------------------------------------------------------'
]

WIN_WIDTH, WIN_HEIGHT = 780, 630
BG_COLOR = (192, 192, 192)
BRICK_WIDTH = BRICK_HEIGHT = 30
BRICK_COLOR = (200, 0, 0)
BRICK_COLOR_2 = (255, 255, 255)
FPS = 60
clock = pygame.time.Clock()
PLAYER_SIZE = 40
BG_SPEED = 3
dx = 0
PLAYER_SPEED = 11
penalty = 0
BTN_W, BTN_H = 220, 60
GOLD = (255, 215, 0)
BLUE = (0, 0, 255, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.display.set_caption('первая игра')
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

player = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
player.set_colorkey((0, 0, 0))


def face(color):
    pygame.draw.circle(player, color, (PLAYER_SIZE // 2, PLAYER_SIZE // 2), PLAYER_SIZE // 2)
    pygame.draw.circle(player, (1, 1, 1), (12, 15), 4)
    pygame.draw.circle(player, (1, 1, 1), (28, 15), 4)
    pygame.draw.circle(player, (255, 0, 0), (20, 23), 4)
    pygame.draw.arc(player, (255, 0, 0), (8, 12, 24, 20), 3.6, 6.0, 3)
    pygame.draw.circle(player, (255, 0, 0), (12, 3), 6)


player_rect = player.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))

text = pygame.font.SysFont('Arial', 22, True, False)
text_xy = ((WIN_WIDTH - text.size(f'штрафных очков: {round(penalty, 1)}')[0]) // 2, 35)

btn = pygame.Surface((BTN_W, BTN_H))
btn.fill(BLUE)
text1 = 'ИГРАТЬ СНОВА?'
text1_xy = text.size(text1)

color = WHITE
face(color)
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_rect.x += PLAYER_SPEED
    if keys[pygame.K_LEFT]:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_UP]:
        player_rect.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player_rect.y += PLAYER_SPEED

    screen.fill(BG_COLOR)
    if color == GOLD:
        color = WHITE
        face(color)

    screen.fill(BG_COLOR)

    if dx > -WIN_WIDTH * 4:
        dx -= BG_SPEED
    else:
        if player_rect.x < WIN_WIDTH - PLAYER_SIZE:
            player_rect.x += PLAYER_SPEED

    x = dx
    y = 0
    for row in level:
        for col in row:
            if col == '-':
                # screen.blit(brick, (x, y))
                brick = pygame.draw.rect(screen, BRICK_COLOR, [x, y, BRICK_WIDTH, BRICK_HEIGHT])
                pygame.draw.rect(screen, BRICK_COLOR_2, [x, y, BRICK_WIDTH, BRICK_HEIGHT], 2)
                if brick.colliderect(player_rect):
                    if color == WHITE:
                        color = GOLD
                        face(color)
                    penalty += 0.1
            x += BRICK_WIDTH
        y += BRICK_HEIGHT
        x = dx

    if player_rect.x < WIN_WIDTH - PLAYER_SIZE:
        screen.blit(player, player_rect)
        screen.blit(
            text.render(f'штрафных очков: {round(penalty, 1)}', True, RED, None), text_xy)
    else:
        screen.blit(btn, ((WIN_WIDTH - BTN_W) // 2, WIN_HEIGHT // 2))
        btn.blit(
            text.render(text1, True, WHITE, None),
            ((BTN_W - text1_xy[0]) // 2, (BTN_H - text1_xy[1]) // 2))
        screen.blit(
            text.render(f'штрафных очков: {round(penalty, 1)}', True, RED, None),
            ((WIN_WIDTH - text.size(f'штрафных очков: {round(penalty, 1)}')[0]) // 2,
             WIN_HEIGHT // 2 - BTN_H))

    pygame.display.set_caption(f' FPS: {round(clock.get_fps(), 2)}')
    pygame.display.update()
    clock.tick(FPS)
