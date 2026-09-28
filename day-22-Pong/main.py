import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

#Screen configuration
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

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
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #Needs to bounce
        ball.bounce_y()

screen.exitonclick()