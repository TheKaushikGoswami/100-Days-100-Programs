# Importing the libraries
import pygame
import time
import random

# Initializing pygame
pygame.init()

# Dimension of window
width = 600
height = 400

# Creating the game window
screen = pygame.display.set_mode((width, height))

# Setting the title and icon
pygame.display.set_caption('Snake Game')

# Frames per second controller
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

# Font styles
font_style = pygame.font.SysFont("calibri", 50)
score_font = pygame.font.SysFont("calibri", 20)

# Function to display the score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, (0, 0, 0))
    screen.blit(value, [0, 0])

# Function to draw the snake
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (0, 255, 0), [x[0], x[1], snake_block, snake_block])

# Function to display a message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# Function for the game loop
def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Defining food parameters
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Button dimensions and colors
    button_width = 100
    button_height = 50
    button_color = (200, 200, 200)
    button_text_color = (0, 0, 0)

    # Quit button coordinates
    quit_button_x = width - button_width - 10
    quit_button_y = 10

    # Restart button coordinates
    restart_button_x = width - button_width - 10
    restart_button_y = quit_button_y + button_height + 10

    # Game loop
    running = True
    while running:

        while game_close:
            screen.fill((0, 0, 0))
            message("You Lost!", (255, 0, 0))

            # Drawing quit button
            pygame.draw.rect(screen, button_color, [quit_button_x, quit_button_y, button_width, button_height])
            quit_text = score_font.render("Quit", True, button_text_color)
            screen.blit(quit_text, (quit_button_x + 20, quit_button_y + 15))

            # Drawing restart button
            pygame.draw.rect(screen, button_color, [restart_button_x, restart_button_y, button_width, button_height])
            restart_text = score_font.render("Restart", True, button_text_color)
            screen.blit(restart_text, (restart_button_x + 10, restart_button_y + 15))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_close = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # Checking if quit button is clicked
                    if quit_button_x <= mouse_x <= quit_button_x + button_width and \
                            quit_button_y <= mouse_y <= quit_button_y + button_height:
                        running = False
                        game_close = False
                    # Checking if restart button is clicked
                    elif restart_button_x <= mouse_x <= restart_button_x + button_width and \
                            restart_button_y <= mouse_y <= restart_button_y + button_height:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Keyboard arrow events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Setting the boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill((255, 255, 255))

        # Drawing the food
        pygame.draw.rect(screen, (0, 0, 0), [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # For snake to not hit its own body
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Checking same coordinates
        if x1 == foodx and y1 == foody:
            # Making food appear at random position
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            # Increasing the length of the snake
            Length_of_snake += 1

        # Setting the frames per second
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
