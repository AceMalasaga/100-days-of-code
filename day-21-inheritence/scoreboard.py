from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        #set the initial score to 0, and white,
        # and center the Score: 0 using goto, and update the scoreboard
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear the scoreboard and update the score"""
        self.clear()
        self.write(f"Score {self.score}", align=ALIGNMENT ,font=FONT)

    def game_over(self):
        self.goto(0,0)
        # self.color("white")
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score by one each time it's eat"""
        self.score += 1
        self.update_scoreboard()