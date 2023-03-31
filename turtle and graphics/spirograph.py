from turtle import Turtle,Screen,colormode
import random
t = Turtle("turtle")
colormode(255)
t.speed(0)
t.pensize(2)

def rand_colour():
    r=(random.randint(0,255))
    g=(random.randint(0,255))
    b=(random.randint(0,255))
    return (r,g,b)

def draw_spirograph(gap_size):
    for i in range(int(360/gap_size)):
        t.color(rand_colour())
        t.circle(100)
        # t.right(gap_size)
        t.setheading(t.heading() + gap_size)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()

# for i in range(36):
#     t.color(rand_colour())
#     t.circle(100)
#     t.right(10)