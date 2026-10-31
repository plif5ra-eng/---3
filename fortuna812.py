# -*- coding: utf-8 -*-
import random
import pygame 
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Kube")
clock = pygame.time.Clock()
#Переменные платформы
platform_x = 350
platform_y = 570
platform_speed = 10
#Переменные мячика
ballSpeed_x = 5
ballSpeed_y = 3
ball_x = 300
ball_y = 10
# Переменная блока
blocks = []
def create_block():
    blocks.clear()
    for row in range(4):
        for col in range(8):
            bx = 50 + col * 90
            by = 50 + row * 30
            blocks.append({"x": bx,"y": by,"width": 80,"height":20,"visible": True})
create_block()

    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((40,40,70))
    
    pygame.draw.rect(screen, (0,200,250), (platform_x,platform_y,200,10))
    pygame.draw.circle(screen, (255,255,255),(ball_x,ball_y), 10)
    
    for block in blocks:
        if block["visible"]:
            pygame.draw.rect(screen,(0,255,0),(block["x"],block["y"],block["width"],block["height"]))
    
    
    
    ball_x = ball_x + ballSpeed_x
    ball_y = ball_y + ballSpeed_y
     
    if ball_y > 0:
        if platform_x <= ball_x <= platform_x + 200 and platform_y <= ball_y + 10 <= platform_y + 10:
            ballSpeed_y = -ballSpeed_y
            ball_y = platform_y - 10
           
    for block in blocks:
        if block["visible"]:
            if ballSpeed_y < 0 and block["y"] + block["height"] <= ball_y - 10 <= block["y"] + block["height"] + 10 and block["x"] <= ball_x <= block["x"] + block["width"]:
                ballSpeed_y = -ballSpeed_y
                block["visible"] = False
                break

    if ball_y > 800:
        print("Проиграл")
        running = False
    if ball_x <= 10 or ball_x >=790:
        ballSpeed_x = -ballSpeed_x
    if ball_y <= 10:
        ballSpeed_y = -ballSpeed_y
    if platform_x < 0:
        platform_x = 0
    if platform_x > 600:
        platform_x = 600   
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        platform_x = platform_x - platform_speed
    if keys[pygame.K_RIGHT]:
        platform_x = platform_x + platform_speed 
        
    pygame.display.flip()
    clock.tick(60)
