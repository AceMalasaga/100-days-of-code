from turtle import Screen, Turtle
from random import randint

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet ", prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
y_coordinates = [-100, -60, -20, 20, 60, 100]
turtles = []

for i in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x=-230, y=y_coordinates[i])
    turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} is the winner!")
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()