import pygame

# Initialize pygame
pygame.init()

# Set display dimensions and base color
display_width = 800
display_height = 600
base_color = (119, 118, 110)

# Load background image and car image
background_img = pygame.image.load("emptyroad.png")
car_img = pygame.image.load('carYY.png')

# Create game display
game_displays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Car Game")

# Set up clock
clock = pygame.time.Clock()

# Define car function
def car(x, y):
    game_displays.blit(car_img, (x, y))

# Define background function
def background():
    game_displays.blit(background_img, (0, 0))

# Define game loop
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    bumped = False

    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        # Fill background with base color
        game_displays.fill(base_color)

        # Call background and car functions
        background()
        car(x, y)

        # Update display
        pygame.display.update()

        # Set frames per second
        clock.tick(60)

# Call game loop function
game_loop()

# Quit pygame
pygame.quit()
quit()
