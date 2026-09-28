import time
from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

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
#Right paddle use Up and Down keys
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")

#Left paddle use w and s keys
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()