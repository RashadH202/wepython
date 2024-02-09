from turtle import Turtle 

ALIGHTMENT = "center"
FONT = ("Courier", 24, "normal")
DATA_FILE = "data.txt"

class Scoreboard(Turtle):
    """A class representing the scoreboard in the snake game."""

    def __init__(self):
        """Initializing the scoreboard object."""
        super().__init__(self)
        self.high_score = self._load_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self._update_scoreboard()

    def _update_scoreboard(self):
        """clear thescoreboard and write the currentscore andhigh score"""
        self.clear()
        self.write(f"score:{self.score} High Score:{self.high_score}", align=ALIGHTMENT, font=FONT)

    def increase_score(self):
        """increase thescore by 1 and update the scoreboard"""
        self.score += 1
        self._update_scoreboard()

    def _load_high_score(self):
        """Load the high score from thedata file."""
        with open(DATA_FILE) as data:
            return int(data.read())
        
    def _update_high_score(self):
        """Update and save the high score if the currrent score is higher than high score"""
        self.high_score = self.high_score
        with open(DATA_FILE, mode="w") as data:
            data.write(f"{self.high_score}")