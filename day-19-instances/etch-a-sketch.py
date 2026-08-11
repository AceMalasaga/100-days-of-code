from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_back():
    tim.backward(10)

def clear_screen():
    #I just used the reset method
    screen.reset()

def clock_wise():
    # I used tim.left(60)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def counter_clock_wise():
    # I used tim.left(60)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=clock_wise)
screen.onkey(key="d", fun=counter_clock_wise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
# import turtle
#
# t=turtle.Turtle()
# t.speed(0)
# colors = ["red", "green", "blue", "yellow", "orange", "purple"]
#
# for i in range(72):
#     t.color(colors[i % 6])
#     t.circle(50)
#     t.left(5)
#
# turtle.done()