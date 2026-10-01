from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move()
        self.move_speed = 0.1

    def move(self):
        """Move the ball in the top right corner"""
        #Add x_cor and y_cor the X_MOVE and Y_MOVE
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        #then go to that location
        self.goto(new_x,new_y)

    def reset_position(self):
        """Reset the position of the ball"""
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1

    def bounce_y(self):
        """Bounce the ball's y-axis"""
        #Multiply 10 by negative 1 which results to have -10
        #Remember positive multiply by negative equals negative, the p * p = p, and n * n = p
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9