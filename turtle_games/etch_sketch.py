from turtle import Turtle,Screen,colormode

t = Turtle()
screen = Screen()
t.speed(10)

def move_forward_letters():
    t.fd(18)
def move_backward_letters():
    t.backward(18)
def change_direction_left_ward_letters():
    t.left(180)
def change_direction_right_ward_letters():
    t.right(180)
def clear_screen_letters():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

 
# keys
def move_forward_keys():
    t.fd(18)
def move_backward_keys():
    t.backward(18)
def change_direction_left_ward_keys():
    t.left(10)
def change_direction_right_ward_keys():
    t.right(10)



screen.listen()
screen.onkey(fun=move_forward_letters,key="w")
screen.onkey(fun=move_backward_letters,key="s")
screen.onkey(fun=change_direction_left_ward_letters,key="a")
screen.onkey(fun=change_direction_right_ward_letters,key="d") 
screen.onkey(fun=clear_screen_letters,key="c") 


screen.onkey(fun=move_forward_keys,key="Up")
screen.onkey(fun=move_backward_keys,key="Down")
screen.onkey(fun=change_direction_left_ward_keys,key="Left")
screen.onkey(fun=change_direction_right_ward_keys,key="Right") 
screen.onkey(fun=clear_screen_letters,key="c") 

screen.exitonclick()