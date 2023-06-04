"""
Author: Tech With Haberjame
GitHub: Tech-With-Haberjame
Tiktok: haberjame
Contact: haberjame.tech@gmail.com
"""

import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

Screen_Width = 600
Screen_Height = 400

Screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption('Snake Game by HaberJame')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("comicsansms", 25)
score_font = pygame.font.SysFont("comicsansms", 25)

def Your_score(score, best_score):
    value = score_font.render("Score: " + str(score), True, red)
    Screen.blit(value, [30, 20])
    rainbow_colors = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)]
    best_score_text = score_font.render("Best Score: " + str(best_score), True, rainbow_colors[int(time.time() * 3) % len(rainbow_colors)])
    Screen.blit(best_score_text, [380, 20])

def load_best_score():
    try:
        with open("best_score.txt", "r") as file:
            best_score = int(file.read())
    except FileNotFoundError:
        best_score = 0
    return best_score

def save_best_score(best_score):
    with open("best_score.txt", "w") as file:
        file.write(str(best_score))

def our_snake(snake_block, snake_list, snake_color):
    for x in snake_list:
        pygame.draw.rect(Screen, snake_color, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    Screen.blit(mesg, [Screen_Width / 6, Screen_Height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = Screen_Width / 2
    y1 = Screen_Height / 2

    x1_change = snake_block
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    snake_color = yellow

    foodx = round(random.randrange(0, Screen_Width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, Screen_Height - snake_block) / 10.0) * 10.0

    best_score = load_best_score()

    while not game_over:

        while game_close:
            Screen.fill(red)
            message("Bad Luck! Press S to Start or Q to Quit", black)
            Your_score(Length_of_snake - 1, best_score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_s:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != snake_block:
                    x1_change = -snake_block
                    y1_change = 0
                
                elif event.key == pygame.K_RIGHT and x1_change != -snake_block:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != snake_block:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -snake_block:
                    y1_change = snake_block
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change

        if x1 >= Screen_Width:
            x1 = 0
        elif x1 < 0:
            x1 = Screen_Width - snake_block
        elif y1 >= Screen_Height:
            y1 = 0
        elif y1 < 0:
            y1 = Screen_Height - snake_block

        Screen.fill(black)
        pygame.draw.rect(Screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List, snake_color)
        Your_score(Length_of_snake - 1, best_score)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, Screen_Width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, Screen_Height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            snake_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if Length_of_snake - 1 > best_score:
            best_score = Length_of_snake - 1
            save_best_score(best_score)

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
