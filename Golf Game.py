import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 15
HOLE_RADIUS = 20
FPS = 60

# these are the variables and colors I am using
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKGREEN = (0, 100, 0)
# these are the inputs that the user will use to play the game
Launch_Angle = int(input("Chose the launch angle of the golf shot: "))
Shot_Power = int(input("Choose the power of the golf shot: "))

# This makes the play screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golf Game")
clock = pygame.time.Clock()

# Golf ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect(center=(WIDTH - 700, HEIGHT - 45))
        self.dx = 0
        self.dy = 0

    def shoot(self, power, angle):
        self.dx = power * math.cos(math.radians(angle))
        self.dy = -power * math.sin(math.radians(angle))

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

# Hole class
class Hole(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((HOLE_RADIUS * 2, HOLE_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, BLACK, (HOLE_RADIUS, HOLE_RADIUS), HOLE_RADIUS)
        self.rect = self.image.get_rect(center=(WIDTH - 50, HEIGHT - 400))

# this is the function to play the game
def handle_events(ball):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball.shoot(Shot_Power, Launch_Angle)  # this is where the user adjusts power and angle as needed

# This is the function that draws the graphics
def draw(ball, hole):
    screen.fill(GREEN)
    pygame.draw.circle(screen, BLUE, (WIDTH - 300, HEIGHT - 70), 95)  # Water hazard
    pygame.draw.circle(screen, BLUE, (WIDTH - 150, HEIGHT - 120), 120)  # Water hazard
    pygame.draw.rect(screen, (139, 69, 19), (0, HEIGHT - 30, WIDTH, 30))  # Ground
    pygame.draw.ellipse(screen, (245, 222, 179), (120, 90, 300, 220))  # (x, y, width, height)
    screen.blit(ball.image, ball.rect)
    screen.blit(hole.image, hole.rect)

# this is the main game loop
def play_golf():
    ball = Ball()
    hole = Hole()
    all_sprites = pygame.sprite.Group(ball, hole)

    while True:
        handle_events(ball)

        ball.update()
        all_sprites.update()

        # Check for the ball going in the hole
        if pygame.sprite.collide_circle(ball, hole):
            print("Congratulations! You made a hole in one!")
            pygame.quit()
            sys.exit()

        if ball.dy >= screen.get_height():
            print("So close, try again")
            pygame.quit()
            sys.exit()


        draw(ball, hole)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    play_golf()