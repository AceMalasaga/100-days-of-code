from turtle import Turtle
# UP = 90
# DOWN = 270
# LEFT = 180
# RIGHT = 0

DOWN = 180
UP = 0
MOVE_DISTANCE = 20
class Paddle:

    def __init__(self):
        self.paddle = None
        self.paddle_configuration()

    def paddle_configuration(self):
        paddle_config = Turtle(shape="square")
        paddle_config.color("white")
        paddle_config.penup()
        paddle_config.shapesize(stretch_wid=5, stretch_len=1)
        paddle_config.goto(350, 0)
        self.paddle = paddle_config

    # def move(self):
    #     self.paddle.forward(MOVE_DISTANCE)
    #
    # def move_up(self):
    #     if self.paddle.heading() != DOWN:
    #         self.paddle.setheading(UP)
    #         self.move()
    #
    # def move_down(self):
    #     if self.paddle.heading() != UP:
    #         self.paddle.setheading(DOWN)
    #         self.move()

    def go_up(self):
        # Get current Y coordinate and add the distance to go UP
        new_y = self.paddle.ycor() + MOVE_DISTANCE
        #Since the movement is only the y-axis replace it with new y-axis
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        # Get current Y coordinate and subtract the distance to go DOWN
        new_y = self.paddle.ycor() - MOVE_DISTANCE
        #Since the movement is only the y-axis replace it with new y-axis
        self.paddle.goto(self.paddle.xcor(), new_y)
