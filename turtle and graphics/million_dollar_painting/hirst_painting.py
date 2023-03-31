from turtle import Turtle,Screen,colormode
import random

colormode(255)
t = Turtle("turtle")
color_list = [(246, 243, 238), (247, 241, 244), (240, 246, 242), (201, 165, 111), (238, 241, 246), (146, 75, 52), (222, 201, 138), (55, 93, 122), (167, 153, 45), (134, 33, 23), (134, 163, 183), (42, 28, 22), (48, 118, 87), (195, 92, 74), (18, 95, 75), (147, 177, 148), (42, 33, 36), (161, 143, 157), (232, 177, 165), (29, 41, 50), (109, 74, 77), (10, 26, 19), (137, 27, 30), (183, 204, 176), (82, 147, 125), (183, 85, 88), (40, 73, 82), (44, 65, 87), (67, 64, 58),
(216, 177, 180)]
t.speed(0)
t.hideturtle()
t.penup()
t.setpos(-230,-220)
for row in range(10):
    for col in range(10):
        t.dot(20,random.choice(color_list))
        t.fd(50)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(500)
    t.right(180)

screen = Screen()
screen.exitonclick()

