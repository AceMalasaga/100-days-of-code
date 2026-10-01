from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-215, 260)
        self.write(f"Level:{self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()