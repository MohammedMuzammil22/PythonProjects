import random
from turtle import Turtle,Screen

# turtle = Turtle()
# turtle.color("CadetBlue")
# turtle.shape("turtle")
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)


# for _ in range(10):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.down()

t = Turtle()
t.shape("turtle")
turtle_colour = ["CadetBlue","CadetBlue1","crimson","silver","green","dark violet","antique white","yellow",'blue']
t.pensize(5)
t.pu()
t.setpos(-20,80)
t.pd()
# function
def draw_shape(no_of_side):
    angle = 360/no_of_side
    t.color(random.choice(turtle_colour))
    for _ in range(no_of_side):
        t.forward(100)
        t.right(angle)

for i in range(3,11):
    draw_shape(i)

# t = Turtle()
# t.color("CadetBlue")
# t.shape("turtle")

# # triangle
# for _ in range(3):
#     t.forward(100)
#     t.right(120)

# t.color("CadetBlue1")

# #square 
# for _ in range(4):
#     t.forward(100)
#     t.right(90)

# t.color("crimson")

# # pentagon
# for _ in range(5):
#     t.forward(100)
#     t.right(72)

# t.color("silver")

# # hexagon
# for _ in range(6):
#     t.forward(100)
#     t.right(60)

# t.color("green")

# # heptagon
# for _ in range(7):
#     t.forward(100)
#     t.right(51.42)

# t.color("dark violet")

# # octagon
# for _ in range(8):
#     t.forward(100)
#     t.right(45)

# t.color("antique white")

# # nanogon
# for _ in range(9):
#     t.forward(100)
#     t.right(40)

# t.color("yellow")

# # decagon
# for _ in range(10):
#     t.forward(100)
#     t.right(36)

screen = Screen()
screen.exitonclick()