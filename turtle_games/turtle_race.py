from turtle import Turtle,Screen,colormode
import random
# colormode(255)

color_list =['indigo','maroon','gold','cyan']
screen = Screen()

user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? select colour")

t1 = Turtle('turtle')
t2 = Turtle('turtle')
t3 = Turtle('turtle')
t4 = Turtle('turtle')
t5 = Turtle('turtle')
# t1.color(random.choice(color_list))
t1.color(user_bet)
t2.color(random.choices(color_list))
t3.color(random.choices(color_list))
t4.color(random.choices(color_list))
t5.color(random.choices(color_list))

t1.penup()
t2.penup()
t3.penup()
t4.penup()
t5.penup()

t1.setpos(-310,100)
t2.setpos(-310,50)
t3.setpos(-310,0)
t4.setpos(-310,-50)
t5.setpos(-310,-100)


# speed = [0,10,6,3,1]
speed_list = [0,1,2,3,4,5,6,7,8,9,10]
# speed_list = [0,1,2,3,4,5,6]
# t1.speed(random.choice(speed_list))
# t2.speed(random.choice(speed_list))
# t3.speed(random.choice(speed_list))
# t4.speed(random.choice(speed_list))
# t5.speed(random.choice(speed_list))
t1.speed(0)
t2.speed(1)
t3.speed(1)
t4.speed(1)
t5.speed(1)

def move_forward(t):
    t.forward(15)

for i in range(41):
    move_forward(t1)
    move_forward(t2)
    move_forward(t3)
    move_forward(t4)
    move_forward(t5)

# print(t1.pos())
# print(t2.pos())
# print(t3.pos())
# print(t4.pos())
# print(t5.pos())

# if(t1.position()==(305.00,100.00) and t1.color==user_bet ):
#     print(f"the winner is {t1.color()} turtle")
#     print("you won the game")

# elif(t2.position()==(305.00,50.00) and t2.color==user_bet):
#     print(f"the winner is {t2.color()} turtle")
#     print("you won the game")

# elif(t3.position()==(305.00,0.00) and t3.color==user_bet):
#     print(f"the winner is {t3.color()} turtle")
#     print("you won the game")

# elif(t4.position()==(305.00,-50.00) and t4.color==user_bet):
#     print(f"the winner is {t4.color()} turtle")
#     print("you won the game")

# elif(t5.position()==(305.00,-100.00) and t5.color==user_bet):
#     print(f"the winner is {t5.color()} turtle")
#     print("you won the game")
# else:
#     print("you have lost the match")



if(t1.xcor==(305.00) and t1.color==user_bet ):
    print(f"the winner is {t1.color()} turtle")
    print("you won the game")

elif(t2.xcor==(305.00) and t2.color==user_bet):
    print(f"the winner is {t2.color()} turtle")
    print("you won the game")

elif(t3.xcor==(305.00) and t3.color==user_bet):
    print(f"the winner is {t3.color()} turtle")
    print("you won the game")

elif(t4.xcor==(305.00) and t4.color==user_bet):
    print(f"the winner is {t4.color()} turtle")
    print("you won the game")

elif(t5.xcor==(305.00) and t5.color==user_bet):
    print(f"the winner is {t5.color()} turtle")
    print("you won the game")
else:
    print("you have lost the match")








screen.exitonclick()