import pygame


pygame.init()

display_width=800
display_height=800
basecolor=(119,118,110)

gamedisplays = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Car Game")

clock=pygame.time.Clock()

def game_loop():
    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                bumped=True 

        gamedisplays.fill(basecolor)
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()



