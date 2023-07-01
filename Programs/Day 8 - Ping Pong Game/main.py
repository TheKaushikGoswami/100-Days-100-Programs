import pygame
import sys
import random

# Initialising the pygame
pygame.init()

# frames per second
c = pygame.time.Clock()

# Dimensions for window
width = 900
height = 600

# creating game window
screen = pygame.display.set_mode((width, height))

# Title and icon
pygame.display.set_caption("Ping Pong Game")

# Game rectangle
ball = pygame.Rect(width / 2 - 15, height / 2 - 15, 30, 30, )
player1 = pygame.Rect(width - 20, height / 2 - 70, 10, 140)
player2 = pygame.Rect(10, height / 2 - 70, 10, 140)

# Game variables
ball_speedx = 6 * random.choice((1, -1))
ball_speedy = 6 * random.choice((1, -1))
player1_speed = 0
player2_speed = 6
player1_score = 0
player2_score = 0


# Function for ball to move
def ball_movement():
    global ball_speedx, ball_speedy, player1_score, player2_score
    ball.x += ball_speedx
    ball.y += ball_speedy

    # Bouncing the ball
    if ball.top <= 0 or ball.bottom >= height:
        ball_speedy *= -1
    if ball.left <= 0:
        player1_score += 1
        ball_restart()
    if ball.right >= width:
        player2_score += 1
        ball_restart()

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speedx *= -1


# function for the movement of player1
def player1_movement():
    global player1_speed
    player1.y += player1_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= height:
        player1.bottom = height


# function for the movement of player2
def player2_movement():
    global player2_speed
    if player2.top < ball.y:
        player2.top += player2_speed
    if player2.bottom > ball.y:
        player2.bottom -= player2_speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= height:
        player2.bottom = height


# Function to reset the ball position
def ball_restart():
    global ball_speedx, ball_speedy
    ball.center = (width / 2, height / 2)
    ball_speedy *= random.choice((1, -1))
    ball_speedx *= random.choice((1, -1))


# Font variable
font = pygame.font.SysFont("calibri", 25)

# Game Loop
while True:
    for event in pygame.event.get():
        # Checking for quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # checking for key pressed event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 8
            if event.key == pygame.K_UP:
                player1_speed -= 8
        # checking for key released event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 8
            if event.key == pygame.K_UP:
                player1_speed += 8

    # calling the functions
    ball_movement()
    player1_movement()
    player2_movement()

    # setting the score condition
    if ball.x < 0:
        player1_score += 1
    elif ball.x > width:
        player2_score += 1

    # Visuals
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (220, 220, 220), player1)
    pygame.draw.rect(screen, (220, 220, 220), player2)
    pygame.draw.ellipse(screen, (220, 220, 220), ball)
    pygame.draw.aaline(screen, (220, 220, 220), (width / 2, 0), (width / 2, height))

    # To draw score font
    player1_text = font.render("Score:" + str(player1_score), False, (255, 255, 255))
    screen.blit(player1_text, [600, 50])
    player2_text = font.render("Score:" + str(player2_score), False, (255, 255, 255))
    screen.blit(player2_text, [300, 50])

    # Updating the game window
    pygame.display.update()

    # 60 frames per second
    c.tick(60)