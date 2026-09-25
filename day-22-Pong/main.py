import time
from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
paddle = Paddle()

#Screen configuration
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#Paddle config
# paddle.shape("square")
# paddle.color("white")
# paddle.penup()
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.goto(350, 0)

screen.listen()
#Don't add the parenthesis, when using function as parameters/arguements
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down,"Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()