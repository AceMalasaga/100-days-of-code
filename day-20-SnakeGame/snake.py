from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments = []
        self.snake_body()

    def snake_body(self):
        for i in range(3):
            snakes = Turtle(shape="square")
            snakes.color("white")
            snakes.penup()
            snakes.goto(x=0 + (i * -20), y=0)
            self.segments.append(snakes)

    def move(self):
        # Normally range takes start and stop, but step defines how to count (in this case, backwards by -1)
        # Start at 2, stop before 0, and step -1 (counts: 2, 1)
        # len(snake) is 3, but the last index is 2 (indexes are 0, 1, 2)
        # Index 3 (len(snake)) would give an IndexError, so we use len(snake) - 1 (which is 2)

        # So in snake[0] is the head, snake[1] is the body, and snake[2] is the tail
        for snake_num in range(len(self.segments) - 1, 0, -1):
            # basically find where the body and tail position
            # first iteration snake_num is 2, so snake_num - 1 = 1
            # snake[1] (body) then find the body X coordinate using the method xcor()
            coordinate_x = self.segments[snake_num - 1].xcor()
            # snake[1] (body) then find the body Y coordinate using the method ycor()
            coordinate_y = self.segments[snake_num - 1].ycor()
            # moves the tail based on where the body coordinate
            # snake[2] (tail)
            self.segments[snake_num].goto(coordinate_x, coordinate_y)
            # iteration 2, find the head position and move it there
        # Move the head forward
        self.segments[0].forward(20)