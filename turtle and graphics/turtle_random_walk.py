from turtle import Turtle,Screen,colormode
import random
t = Turtle("turtle")
direction = [90,180,270,360]
turtle_colour = ["CadetBlue","CadetBlue1","crimson","silver","green","dark violet","antique white","yellow",'blue']

t.speed(10)
t.pensize(15)
colormode(255) #to change colour

def random_walk(rand_direction):
    # t.pencolor((,random.randint(0,255),random.randint(0,255)))
    # t.color(random.choice(turtle_colour))
    t.right(rand_direction)
    t.forward(50)

for _ in range(500):
    r=(random.randint(0,255))
    g=(random.randint(0,255))
    b=(random.randint(0,255))
    t.color((r,g,b))
    random_walk(random.choice(direction))


screen = Screen()
screen.exitonclick()