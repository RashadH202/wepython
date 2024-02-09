from turtle import Turtle
import random 
class Food(Turtle):
    """A Class representing the food is the snake game"""

    #constants for the screen boundaries
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

    def __init__(self):
        """initialize the food object"""
        super().__Init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """move the food to a randomlocation on the screem"""
        random_x = random.randint(-self.SCREEN_WIDTH // 2 + 20, self.SCREEN_WIDTH // 2 - 20)
        random_y = random.randint(-self.SCREEN_HEIGHT // 2 + 20, self.SCREEN_HEIGHT // 2 - 20)
        self.goto(random_x, random_y)

        