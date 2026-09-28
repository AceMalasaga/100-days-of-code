from turtle import Turtle

DOWN = 180
UP = 0
MOVE_DISTANCE = 20
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        # paddle_config.goto(350, 0)
        self.goto(position)

    def go_up(self):
        # Get current Y coordinate and add the distance to go UP
        new_y = self.ycor() + MOVE_DISTANCE
        #Since the movement is only the y-axis replace it with new y-axis
        self.goto(self.xcor(), new_y)

    def go_down(self):
        # Get current Y coordinate and subtract the distance to go DOWN
        new_y = self.ycor() - MOVE_DISTANCE
        #Since the movement is only the y-axis replace it with new y-axis
        self.goto(self.xcor(), new_y)
