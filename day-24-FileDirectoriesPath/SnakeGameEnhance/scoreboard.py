from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        #set the initial score to 0, and white,
        # and center the Score: 0 using goto, and update the scoreboard
        self.score = 0
        # self.high_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        # file = open("data.txt", "r")
        # self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear the scoreboard and update the score"""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT ,font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     # self.color("white")
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score by one each time it's eat"""
        self.score += 1
        self.update_scoreboard()