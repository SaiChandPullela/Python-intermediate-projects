from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
x = 300

class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_choice = random.randint(1, 5)
        if random_choice == 1:
            car = Turtle()
            car.penup()
            car.shape('square')
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.goto(x, random.randint(-250, 250))
            self.cars.append(car)
        self.move_forward()

    def move_forward(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT









