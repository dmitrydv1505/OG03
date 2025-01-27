import pygame
import random


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра тир")
icon = pygame.image.load("img/tir.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_heigh = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_heigh)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

score = 0

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_heigh:
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_heigh)
    target_x += 1
    if target_x > SCREEN_WIDTH:
        target_x = 0
        target_y = random.randint(0, SCREEN_HEIGHT - target_heigh)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()
pygame.quit()



