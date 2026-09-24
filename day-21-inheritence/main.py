from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#Set the screen
screen = Screen()
#Set the screen width and height to 600
screen.setup(width=600, height=600)
#Set screen color to black
screen.bgcolor("black")
#Set the title to whatever you named it
screen.title("The Bitin Game")
#Remove the animation like turning the segment to a different direction
screen.tracer(0)

#Call each class
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Snake controller, using keystroke
screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")

#Set the game True
game_is_on = True
while game_is_on:
    #Set the screen update to manually refresh the screen to show the drawing, since we set the tracer 0 which hide the drawing
    screen.update()

    #Set the time pause
    time.sleep(0.1)

    #Constantly moving the snake
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        #if the distance is True, call the method of scoreboard increase_score
        scoreboard.increase_score()
        #Refresh the food by calling the refresh method in food
        snake.extend()
        food.refresh()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    #Slice the first segment to skip from the first value and start from the 2nd
    for segment in snake.segments[1:]:
        #Get rid of if segment pass since I use slice
        # if segment == snake.head:
        #     pass
        # elif snake.head.distance(segment) < 5:
        #     game_is_on = False
        #     scoreboard.game_over()
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()