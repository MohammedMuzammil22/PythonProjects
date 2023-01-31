import random

availableChoice = ['rock','paper','sissor']
winningScore = 5

def userInput():
    while(True):
        userIP = int(input("""
SELECT
1.Rock
2.Paper
3.Sissor
Enter your choice: """))
        if( 1<= userIP <= 3):
            return availableChoice[userIP-1]

def computerChoice():
    return random.choice(availableChoice)

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

def checkWin(userScore,computerScore,name):
    if(userScore==winningScore):
        print(f"{name} wins...")
        return 1
    
    elif(computerScore==winningScore):
        print(f"Computer wins...")
        return 1

def game():
    while(True):
        userScore=0
        computerScore=0
        print("""__________Welcome to Rock_Paper_Sisors__________""")
        name = input("Enter your name: ")
        while(True):
            userChoice = userInput()
            compChoice = computerChoice()
            userScore,computerScore = RPS_conditions(userChoice,compChoice,userScore,computerScore)
            displayScore(userScore,computerScore,name,userChoice,compChoice)
            win = checkWin(userScore,computerScore,name)
            if(win == 1):
                break
        play = input("Do you want to play again (yes/no): ")
        if(play.lower() == 'no'):
            break

game()

