import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("pong")


ball_pos = [400, 300]
ball_vel = [0.5, 0.5]

paddle1_pos = [50, 250]
paddle2_pos = [750, 250]
paddle_size = [10 ,100]
paddle_speed = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_pos[1] -= paddle_speed
    if keys[pygame.K_s]:
        paddle1_pos[1] += paddle_speed
    if keys[pygame.K_UP]:
        paddle2_pos[1] -= paddle_speed
    if keys[pygame.K_DOWN]:
        paddle2_pos[1] += paddle_speed

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    if ball_pos[1] <= 0 or ball_pos[1] >= 600:
        ball_vel[1] = -ball_vel[1]

    if (ball_pos[0] <= paddle1_pos[0] + paddle_size[0] and
        paddle1_pos[1] < ball_pos[1] < paddle1_pos[1] + paddle_size[1]):
        ball_vel[0] = -ball_vel[0]
    if (ball_pos[0] >= paddle2_pos[0] - paddle_size[0] and
        paddle2_pos[1] < ball_pos[1] < paddle2_pos[1] + paddle_size[1]):
        ball_vel[0] = -ball_vel[0]

    screen.fill((0,0,0))

    pygame.draw.circle(screen, (255,255,255), ball_pos, 10)
    pygame.draw.rect(screen, (255,255,255), (*paddle1_pos, *paddle_size))
    pygame.draw.rect(screen, (255,255,255), (*paddle2_pos, *paddle_size))

    pygame.display.flip()
    