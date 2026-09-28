from turtle import Turtle

#Make it a global, since this is constant
X_MOVE = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move = 10
        self.move()

    def move(self):
        """Move the ball in the top right corner"""
        #Add x_cor and y_cor the X_MOVE and Y_MOVE
        new_x = self.xcor() + X_MOVE
        new_y = self.ycor() + self.y_move

        #then go to that location
        self.goto(new_x,new_y)

    def bounce_y(self):
        """Bounce the ball's y-axis"""
        #Multiply 10 by negative 1 which results to have -10
        #Remember positive multiply by negative equals negative, the p * p = p, and n * n = p
        self.y_move *= -1