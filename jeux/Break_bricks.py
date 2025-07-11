import pygame
import sys

# Initialisation
pygame.init()

# Constantes
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRICK_COLOR = (200, 0, 0)
PADDLE_COLOR = (0, 200, 0)
BALL_COLOR = (0, 0, 200)

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
BALL_RADIUS = 10

# Fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Casse-brique")

# Balle
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS*2, BALL_RADIUS*2)
ball_speed = [4, -4]

# Raquette
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 0
PADDLE_MOVE_SPEED = 8

# Briques
bricks = []
brick_rows = 5
brick_cols = 10
brick_width = WIDTH // brick_cols
brick_height = 30

for row in range(brick_rows):
    for col in range(brick_cols):
        brick = pygame.Rect(col * brick_width + 1, row * brick_height + 1, brick_width - 2, brick_height - 2)
        bricks.append(brick)

# Boucle principale
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    # Événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_speed = -PADDLE_MOVE_SPEED
            if event.key == pygame.K_RIGHT:
                paddle_speed = PADDLE_MOVE_SPEED
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                paddle_speed = 0

    # Déplacer la raquette
    paddle.x += paddle_speed
    if paddle.left < 0:
        paddle.left = 0
    if paddle.right > WIDTH:
        paddle.right = WIDTH

    # Déplacer la balle
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Collisions murs
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] *= -1
    if ball.top <= 0:
        ball_speed[1] *= -1
    if ball.bottom >= HEIGHT:
        print("Perdu !")
        pygame.quit()
        sys.exit()

    # Collision raquette
    if ball.colliderect(paddle):
        ball_speed[1] *= -1

    # Collision briques
    hit_index = ball.collidelist(bricks)
    if hit_index != -1:
        hit_brick = bricks.pop(hit_index)
        ball_speed[1] *= -1

    # Dessiner raquette, balle, briques
    pygame.draw.rect(screen, PADDLE_COLOR, paddle)
    pygame.draw.ellipse(screen, BALL_COLOR, ball)
    for brick in bricks:
        pygame.draw.rect(screen, BRICK_COLOR, brick)

    # Vérifier victoire
    if not bricks:
        print("Bravo ! Tous les briques sont cassées !")
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(60)
