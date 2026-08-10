# # from turtle import Turtle, Screen
# from colorgram import colorgram
#
# # tortoise  = Turtle()
# # #shape the object to an arrow
# # tortoise .shape("classic")
# # screen = Screen()
#
# colors = colorgram.extract('image.jpg', 19)
# rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb.append(new_color)
# print(rgb)
# from turtle import Turtle, Screen
# from random import choice
#
#
# color_list = [(253, 251, 247), (253, 248, 252), (235, 252, 243), (198, 13, 32),
#               (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69),
#               (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15),
#               (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120),
#               (68, 10, 31), (61, 15, 8), (223, 141, 206)]
#
# def random_color():
#     color = choice(color_list)
#     return color
#
# screen = Screen()
# screen.colormode(255)
# ace = Turtle()
# ace.shape("classic")
# for row in range(10):
#     # lift the pen, so it will not draw
#     ace.penup()
#     # place the arrow to absolute position then add row * 50 to move up the dot
#     ace.goto(-225, -225 + (row * 50))
#     # pen down so it resume drawing
#     ace.pendown()
#     for col in range(10):
#         ace.dot(20, random_color())
#         ace.penup()
#         ace.forward(50)
#         ace.hideturtle()
# screen.exitonclick()


#Instructor code
import turtle as turtle_module
from random import choice

turtle_module.colormode(255)
tim = turtle_module.Turtle()

color_list = [(253, 251, 247), (253, 248, 252), (235, 252, 243), (198, 13, 32),
              (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69),
              (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15),
              (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120),
              (68, 10, 31), (61, 15, 8), (223, 141, 206)]

number_dot = 100
tim.penup()
tim.speed("fastest")
tim.hideturtle()
tim.setheading(220)
tim.forward(310)
tim.setheading(0)

for dot_count in range(1, number_dot + 1):
    tim.dot(20, choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()