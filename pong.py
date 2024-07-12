import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Collisions with the wall
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    
    if ball.left <= 0:
        if score_time is not None and pygame.time.get_ticks() - score_time >= 1000:
            player_score += 1
            score_time = None  # Reset score_time after updating score
            ball_restart()  # Restart ball after scoring
    
    if ball.right >= screen_width:
        if score_time is not None and pygame.time.get_ticks() - score_time >= 1000:
            opponent_score += 1
            score_time = None  # Reset score_time after updating score
            ball_restart()  # Restart ball after scoring

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y, score_time
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))  
    score_time = pygame.time.get_ticks()  # Update score_time to current time

# Initializing pygame
pygame.init()
clock = pygame.time.Clock()

# Setting the height of the window
screen_width = 1279
screen_height = 625

# Display surface on which we will draw everything
screen = pygame.display.set_mode((screen_width, screen_height))

# The title of the window
pygame.display.set_caption('Pong Game')

# Declares the ball
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
# Declares the player
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
# Declares the opponent
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

# Setting the background color
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# Speed of the ball vertically and horizontally
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

# Text Vars
player_score = 0
opponent_score = 0
# Font
game_font = pygame.font.Font("freesansbold.ttf", 32)

# Ball release timer
score_time = pygame.time.get_ticks()  # Initialize score_time

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_animation()

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
    
    # Displaying the player's score
    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (660, 325))
    # Showing the opponent's score
    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (600, 325))

    pygame.display.flip()
    clock.tick(60)
