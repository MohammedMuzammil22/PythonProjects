import turtle 
import pandas

screen = turtle.Screen()
screen.title("US-States-Game")
image = "india.gif"
screen.addshape(image)
turtle.shape(image)
writing_turtle = turtle.Turtle()
writing_turtle.hideturtle()

data = pandas.read_csv("./states_of_india.csv")
state_list = data.state.to_list()
game_is_on =True
score = 0
correct_guess = []
missing_states = []

while(score < 28):
    user_guess = screen.textinput(title=f"{score}/{28}Guess the state", prompt="Guess the name of the State: ").title()
    if(user_guess in state_list and user_guess not in correct_guess):
        print("correct answer")
        score += 1
        correct_guess.append(user_guess)
        current_state_details = data[data.state == user_guess]
        x = int(current_state_details.x)
        y = int(current_state_details.y)
        writing_turtle.penup()
        writing_turtle.goto(x,y)
        writing_turtle.write(f"{user_guess}")
        
    if(user_guess == "Exit"):
        for state in state_list:
            if(state not in correct_guess):
                missing_states.append(state)
        missed_states = pandas.DataFrame(missing_states)
        missed_states.to_csv("missed_states_names.csv")
        break



screen.exitonclick()


# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()