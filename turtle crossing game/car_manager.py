from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10
STARTING_X_POSITION = 310

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.initial_move_distance = 5

        
    def generate_car(self):
        y = random.randint(-250,250)
        self.add_car_segment(y)

    def add_car_segment(self,y):
        random_chance = random.randint(1,6)
        if(random_chance == 1):
            new_car = Turtle()
            new_car.penup()
            new_car.goto(STARTING_X_POSITION,y)
            new_car.setheading(180)
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.initial_move_distance)
    
    def increase_car_speed(self):
        self.initial_move_distance += MOVE_INCREMENT

    
    

