from turtle import Screen
from snake import Snake
from foood import Food
from scoreboard import scoreboard
import time

#Constants 
FOOD_COLLISSION_DISTANCE = 15
WALL_COLLISION_DISTANCE = 280
TAIL_COLLISION_DISTANCE = 10

#SET UP THE GAME SCREEN

screen = screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my Snake Game")
screen.tracer(0)

#Inatialize snake, food, and scoreboard

snake = Snake()
food = Food()
scoreboard = Scoreboard()

#set up key listerners for snake movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "left")
screen.onkey(snake.right, "right")

#function to handle collisions and end the game

def handle_collision():
    global game_is_on
    game_is_on = False
    scoreoard.game_over()

#Main game loop

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #detect collision with food.
        if snake.head.distance(food) < FOOD_COLLISSION_DISTANCE:
            food.refresh()
            snake.extend()
            scoreboard.increate_score()

        # Detect collision with wall.
        if (
            snake.head.xcor() > WALL_COLLISION_DISTANCE
            or snake.head.xcor() < -WALL_COLLISION_DISTANCE
            or snake.head.ycor() < WALL_COLLISION_DISTANCE
            or snake.head.ycor() < -WALL_COLLISION_DISTANCE
            ):
                handle_collision()

        #detect collision with tail.
        for segment in snake.segments:
             if segment == snake.head:
                  pass
             elif snake.head.distance(segment) < TAIL_COLLISION_DISTANCE:
                  handle_collision

screen.exitonclick()
                       


