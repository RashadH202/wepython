#run game after you put the entire code

import pygame

## let computer now you're run a pygame app
pygame.init()

## its good practice to put numbers in variables, so it makes it easier to keep track of what's going on. and to make quick changes. 
display_width=800
display_height=600
basecolor=(119,118,110)

## Create background
backgroundimg=pygame.image.load("emptyroad.png")

def background():
    gamedisplays.blit(backgroundimg,(0,0))
## Creating the car for the game to use
carimg=pygame.image.load('carYY.png')
def car(x,y):
    gamedisplays.blit(carimg,(x,y))

## this sets the game display, ensure you use pygame to let the app now your using their display
gamedisplays = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Car Game")

## Set an clock for your game, it's based off when you start the app
clock=pygame.time.Clock()

## game loop is used to init the app, and to provide it with in game functions.
def game_loop():
## Location for the car on your game canvas
    x=(display_width*0.45)
    y=(display_height*0.8)
    x_change=0



## let the app now the game is going to be open until it's quit
    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                bumped=True

## Car Function through if statments, lets the game know we want the sprite to move left to right
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
## intilizing the change keys to work
        x+=x_change

## change color of displays
        gamedisplays.fill(basecolor)
        

## Call to the car function, all your display function should be called before your display update function
        background()
        car(x,y)
        pygame.display.update()
        clock.tick(60)


## Call Game loop function & function to end the game.

   
game_loop()
pygame.quit()
quit()



