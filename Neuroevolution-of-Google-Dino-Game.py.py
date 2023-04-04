import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

pygame.display.set_caption("Google Dino Game")

# Load necessary images and resources
dino_image = pygame.image.load('.\dino.png')
ground_image = pygame.image.load('.\ground.png')
cactus_image = pygame.image.load('.\cactus.png')

# Add score variable
score = 0
font = pygame.font.Font(None, 36)
game_over = False

#Cactus class
class Cactus:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = cactus_image
        self.speed = 8

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.x -= self.speed
        if self.x < -self.width:
            self.x = screen_width

#Dino class
class Dino:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = dino_image
        self.velocity = 0
        self.gravity = 1

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

        # Prevent the dino from falling below the ground
        if self.y > 200:
            self.y = 200
            self.velocity = 0

    def jump(self):
        if self.y == 200:
            self.velocity = -15

#Ground class
class Ground:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = ground_image

    def draw(self, screen):
        screen_width, _ = screen.get_size()
        for x_offset in range(0, screen_width, self.width):
            screen.blit(self.image, (self.x + x_offset, self.y))

# Initialize the game elements
dino = Dino(50, 200, 50, 50)
ground = Ground(0, 235, 800, 50)
cactus = Cactus(800, 200, 50, 50)

clock = pygame.time.Clock()

def display_game_over(screen, score):
    game_over_text = font.render("Game Over!", True, (0, 0, 0))
    score_text = font.render(f'Final Score: {score}', True, (0, 0, 0))
    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, screen_height // 2 + game_over_text.get_height()))


def display_score(screen, score, font):
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

font = pygame.font.Font(None, 36)


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                dino.jump()
    screen.fill((255, 255, 255))

    # Display the current score
    display_score(screen, score, font)

    if not game_over:
        # Update and draw game elements on the screen
        ground.draw(screen)
        dino.update()
        dino.draw(screen)
        cactus.update()
        cactus.draw(screen)

        # Update the score
        score += 1


        # Check for collisions
        dino_rect = pygame.Rect(dino.x, dino.y, dino.width, dino.height)
        cactus_rect = pygame.Rect(cactus.x, cactus.y, cactus.width, cactus.height)

        if dino_rect.colliderect(cactus_rect):
            print("Game Over!")
            game_over = True

    if game_over:
        display_game_over(screen, score)

        # Update the game display
    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
