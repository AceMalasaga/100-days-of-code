import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
turtle = Turtle()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#Screen configuration
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

#Hide arrow
turtle.hideturtle()
#Tract keyboard stoke
screen.listen()
screen.onkey(player.go_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    #Create a car each loop and move it
    car_manager.create_cars()
    car_manager.car_move()

    #Detect collision with car, use for loop to detect each car collision
    for car in car_manager.cars:
        #if the turtle is closer below 20 pixel "Game Over"
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    #Check the turtle if it's already finish
    if player.is_at_finish_line():
        #If return True, Speed up the cars
        car_manager.car_speed_up()
        scoreboard.increase_score()


screen.exitonclick()