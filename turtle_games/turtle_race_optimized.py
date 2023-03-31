from turtle import Turtle,Screen,colormode
import random

color_list =['indigo','maroon','gold','cyan',"purple"]
screen = Screen()

user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? select colour")
y_coordnites = [100,50,0,-50,-100]
turtle_objects = []

for turtle_index in range(5):
    new_turtle = Turtle("turtle")
    new_turtle.color(color_list[turtle_index])
    new_turtle.penup()
    new_turtle.setpos(x=-310,y=y_coordnites[turtle_index])
    turtle_objects.append(new_turtle)

turtle1=random.choice(turtle_objects)
turtle1.color(user_bet)

if(user_bet):
    is_game_on = True
    
while is_game_on:
    for turtle in turtle_objects:
        if(turtle.xcor()>305.00):
            is_game_on = False
            winning_colour = turtle.pencolor()
            if(winning_colour==user_bet):
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")
        turtle_distance=random.randint(0,10)
        turtle.forward(turtle_distance)

screen.exitonclick()