from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        #set the initial score to 0, and white,
        # and center the Score: 0 using goto, and update the scoreboard
        self.score = 0
        self.color("white")
        self.goto(-40, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear the scoreboard and update the score"""
        self.clear()
        self.write(f"Score {self.score}",  font=("Courier", 18, "normal"))

    def increase_score(self):
        """Increase the score by one each time it's eat"""
        self.score += 1
        self.update_scoreboard()