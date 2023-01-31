import random

def userInput():
    userIP = int(input("""
SELECT
1.Rock
2.Paper
3.Sissor
Enter your choice: """))
    while(userIP<1 or userIP>3):
        userIP = int(input("""
SELECT
1.Rock
2.Paper
3.Sissor
Enter your choice: """))
    AvailableChoice = ['rock','paper','sissor']
    userChoice = AvailableChoice[userIP-1]
    return userChoice

def computerChoice():
    AvailableChoice = ['rock','paper','sissor']
    randomNumber = random.randint (0,2)
    compChoice = AvailableChoice[randomNumber]
    return compChoice

def RPS_conditions(userChoice,compChoice,userScore,computerScore):
    if((userChoice=='rock' and compChoice=='sissor') or (userChoice=='paper' and compChoice=='rock') or (userChoice=='sissor' and compChoice=='paper')):
        userScore += 1
    elif((userChoice=='sissor' and compChoice=='rock') or (userChoice=='rock' and compChoice=='paper') or (userChoice=='paper' and compChoice=='sissor')):
        computerScore += 1
    return[userScore,computerScore]

def displayScore(userScore,computerScore,name,userChoice,compChoice):
    print("___________ ______________ ___________")
    print(f"\n{name}'s choice is :{userChoice}")
    print(f"Computer's choice is :{compChoice}")
    print(f"{name}'s score is :{userScore}")
    print(f"Computer's score is :{computerScore}")
    print("___________ ______________ ___________")

def win(userScore,computerScore,name):
    if(userScore==5):
        print(f"{name} wins...")
        return 1
    
    if(computerScore==5):
        print(f"Computer wins...")
        return 1

def game():
    play=""
    while(play.lower() != 'no'):
        userScore=0
        computerScore=0
        print("""__________Welcome to Rock_Paper_Sisors__________""")
        name = input("Enter your name: ")
        while(True):
            userChoice = userInput()
            compChoice = computerChoice()
            userScore,computerScore = RPS_conditions(userChoice,compChoice,userScore,computerScore)
            displayScore(userScore,computerScore,name,userChoice,compChoice)
            win1 = win(userScore,computerScore,name)
            if(win1==1):
                break
        play = input("Do you want to play again (yes/no): ")

game()

