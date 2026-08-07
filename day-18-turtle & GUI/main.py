from turtle import Turtle, Screen

ace = Turtle()
#shape the object to an arrow
ace.shape("classic")

#Use built in method of turtle to move and turn
#Draw a square challenge 1
#I create a for loop and set the loop to start at 0 and end before 4
# for _ in range(0,4):
#     ace.right(90)
#     ace.forward(100)

#Challenge 2: Draw a dash line
#the range is 10
# for _ in range(10):
#     #penup means the pen will not right basically a blank
#     ace.penup()
#     #then move forward 10 pace. this is still blank
#     ace.forward(10)
#     #pendown means write
#     ace.pendown()
#     #write it in 10 pace since the pen is down
#     ace.forward(10)

#The first attempt is I for loop each shapes which I noticed that it's inefficient
#Import the choice random
# from random import choice
#Set the degree to 3 since triangle is the first shapes and has 3 sides
# degree_angle = 3
#get the color in the Tkinter and stored it in a list
# color = ["CadetBlue", "red", "DarkGreen", "DeepSkyBlue", "DeepPink2",
#               "coral2", "burlywood4", "DarkOrchid4"]
#create awhile base on the degree_angle
# while degree_angle <= 10:
      #get the random color
#     rand_color = choice(color)
      #pass the degreen angle in the for loop
#     for _ in range(degree_angle):
          #degree angle formula
#         degree = 360 / degree_angle
          #use color method and pass the rand_color
#         ace.color(rand_color)
#         ace.forward(100)
#         ace.right(degree)
#     degree_angle += 1

#this is the course solution
# from random import choice
# colour = ["CadetBlue", "red", "DarkGreen", "DeepSkyBlue", "DeepPink2",
#               "coral2", "burlywood4", "DarkOrchid4"]
#
# def draw_shape(number_side):
#     angle = 360 / number_side
#     for _ in range(number_side):
#         ace.forward(100)
#         ace.right(angle)
#
# for side_angle_n in range(3, 11):
#     ace.color(choice(colour))
#     draw_shape(side_angle_n)

#Challenge 4
from random import choice, randint
# screen = Screen()
# screen.colormode(255)
# def random_colour():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     return (r, g, b)
#
# def random_angle():
#     angle = [0, 90, 180, 270]
#     rand_angle = choice(angle)
#     return rand_angle
#
# ace.pensize(5)
# ace.speed("fastest")
#
# for _ in range(200):
#     ace.color(random_colour())
#     ace.forward(15)
#     ace.setheading(random_angle())


#Challenge 5
from random import choice, randint
screen = Screen()
screen.colormode(255)
def random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

# ace.pensize(2)
ace.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        ace.color(random_colour())
        ace.circle(100)
        ace.setheading(ace.heading() + size_of_gap)
draw_spirograph(5)

#Place screen object at the bottom after all the code of turtle completed
#If you place this above, it only executes the code above it.
screen.exitonclick()
