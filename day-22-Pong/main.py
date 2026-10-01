import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

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
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #Needs to bounce
        ball.bounce_y()

    #Detect collision with r_paddle

    # Detect collision with r_paddle using a 50-pixel circular radius.
    # Since a circle sticks out too far horizontally, 'ball.xcor() > 320'
    # ensures the ball is physically close to the paddle before it bounces.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()