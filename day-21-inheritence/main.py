from turtle import Screen
import time
from snake import Snake

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

#Call the Snake class
snake = Snake()
#Set the screen to listen so it will capture keyboard event
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
    #
    time.sleep(0.1)
    snake.move()


screen.exitonclick()