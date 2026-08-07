# from turtle import Turtle, Screen
from colorgram import colorgram

# tortoise  = Turtle()
# #shape the object to an arrow
# tortoise .shape("classic")
# screen = Screen()

colors = colorgram.extract('image.jpg', 19)
rgb = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb.append(new_color)
print(rgb)