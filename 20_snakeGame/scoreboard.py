from turtle import Turtle
ALIGHTMENT = "center"
FONT = ("courier", 24, "normal")
DATA_FILE = data.txt

class Scoreboard(Turtle):
    """A class representing the scoreboard in the snake game"""

    def __Init__(self):
        """Initialize the scoreboard object"""

        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hidetutrle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """clear scoreboard and erite the current score and high score."""
        self.clear()
        self.write(f"Score: {self.score} high score: {self.high_score}", align=ALIGHTMENT, font=FONT)
    
    def reset(self):
        """reset the score and updateteh scoreboard. update high score if needed"""
        if self.score > self.high_score:
            self.update_high_score()
            self.score = 0 
            self.update_scoreboard()

    def increase_score(self):
        """load the high score from the date file"""
        with open(DATA_FILE) as data:
            return int(data.read())
        
    def update_high_score(self):
        "update and save high score to text doc if the high score is beat"
        self.high_score = self.score
        with open(DATA_FILE, MODE="w") as data:
            data.write(str(self.high_score))
