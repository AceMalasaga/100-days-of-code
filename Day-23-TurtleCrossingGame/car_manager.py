from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        """Creates new cars and adds them to the list"""
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.goto(300, randint(-240, 240))
            self.cars.append(new_car)

    def car_move(self):
        """Moves cars backwards and speeed increase on each level"""
        for car in self.cars:
            car.backward(self.car_speed)

    def car_speed_up(self):
        """Increase the speed of each car"""
        self.car_speed += MOVE_INCREMENT