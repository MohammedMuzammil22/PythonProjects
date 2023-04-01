import turtle 
import pandas

screen = turtle.Screen()
screen.title("US-States-Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writing_turtle = turtle.Turtle()
writing_turtle.hideturtle()


data = pandas.read_csv("./50_states.csv")
state_list = data.state

game_is_on =True
score = 0
correct_guess = []

while(game_is_on):
    user_guess = screen.textinput(title=f"{score}/{50}Guess the state", prompt="Guess the name of the State: ").lower()
    for state in state_list:
        if(user_guess==state.lower() and user_guess not in correct_guess):
            print("correct answer")
            score += 1
            correct_guess.append(state.lower())
            current_state_details = data[data.state == state]
            x = int(current_state_details.x)
            y = int(current_state_details.y)
            writing_turtle.penup()
            writing_turtle.goto(x,y)
            writing_turtle.write(f"{state}")
            break
    if score>= 50 :
        game_is_on = False
    

screen.exitonclick()