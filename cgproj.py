import pygame
import os
from random import randrange


os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 800, 800
FPS = 60


pygame.init()
screen = pygame.display.set_mode(RES)
pygame.display.set_caption("Snowfall")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 30, bold=True)

ball_surface = pygame.image.load('ball.png').convert_alpha()
ball_position = (150, 150)
ball_mask = pygame.mask.from_surface(ball_surface)

snowflake_surf = pygame.image.load('snowflake.png').convert_alpha()
snowflake_overlay_surf = pygame.image.load('snowflake.png').convert_alpha()

snowflakes = []


# Snowflakes
for _ in range(100):
    xs0 = randrange(0, WIDTH, 25)
    ys0 = randrange(0, HEIGHT, 15)
    snowflake_rect = snowflake_surf.get_rect(center=(xs0, ys0))
    snowflake_mask = pygame.mask.from_surface(snowflake_surf)
    snowflakes.append([snowflake_rect, snowflake_mask, xs0, ys0])


k = 0
running = True
while running:
    clock.tick(FPS)
    screen.fill('coral')

    pygame.draw.circle(screen, 'WHITE', (WIDTH // 2, HEIGHT // 2), 255, 6)


    for snowflake in snowflakes:
        snowflake_rect = snowflake[0]
        snowflake_mask = snowflake[1]

        snowflake_rect[1] += 1

        if snowflake_rect[1] > HEIGHT:
            snowflake_rect[0] = randrange(0, WIDTH, 25)
            snowflake_rect[1] = randrange(-50, 0, 15)

        offset_x = ball_position[0] - snowflake_rect.left
        offset_y = ball_position[1] - snowflake_rect.top
        if snowflake_mask.overlap(ball_mask, (offset_x, offset_y)):
            new_mask = snowflake_mask.overlap_mask(ball_mask, (offset_x, offset_y))
            new_surface = new_mask.to_surface()
            new_surface.set_colorkey('black')
            screen.blit(new_surface, snowflake_rect)


    pygame.display.update()
    k += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False