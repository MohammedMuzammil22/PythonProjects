from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        # random_x = random.randint(-280,280)
        # random_y = random.randint(-280,280)
        # self.setpos(x=random_x, y=random_y)#goto
        self.update_food_location()
        # self.snake_head_current_pos=snake_obj.head.position()

    # def collision_with_food(self):
    #     if(self.snake_head_current_pos==self.position()):
    #         print("hit")

    def update_food_location(self):
        self.new_random_x = random.randint(-280,280)
        self.new_random_y = random.randint(-280,280)
        self.setpos(x=self.new_random_x, y=self.new_random_y)



