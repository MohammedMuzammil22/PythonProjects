import random

name = input("Enter your name: ")

x=""
while(x.lower()!="no"):
    score = 0
    while(True):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        print(d1)
        print(d2)
        if(d1==1):
            print('''
             ________
            |        |
            |   🌑   |
            |        |
            |________|''', end='     ')
        elif(d1==2):
            print('''
             ________
            |        |
            |  🌑    |
            |    🌑  |
            |________|''', end='     ')
        elif(d1==3):
            print('''
             ________
            | 🌑     |
            |   🌑   |
            |     🌑 |
            |________|''', end='     ')
        elif(d1==4):
            print('''
             ________
            | 🌑  🌑 |
            |        |
            | 🌑  🌑 |
            |________|''', end='     ')
        elif(d1==5):
            print('''
             ________
            | 🌑  🌑 |
            |   🌑   |
            | 🌑  🌑 |
            |________|''', end='     ')
        elif(d1==6):
            print('''
             ________
            | 🌑  🌑 |
            | 🌑  🌑 |
            | 🌑  🌑 |
            |________|''', end='     ')

        if(d2==1):
            print('''
             ________
            |        |
            |   🌑   |
            |        |
            |________|
        ''')
        elif(d2==2):
            print('''
                         ________
                        |        |
                        |  🌑    |
                        |    🌑  |
                        |________|
         ''')
        elif(d2==3):
            print('''
             ________
            | 🌑     |
            |   🌑   |
            |     🌑 |
            |________|
        ''')
        elif(d2==4):
            print('''
                         ________
                        | 🌑  🌑 |
                        |        |
                        | 🌑  🌑 |
                        |________|
                ''')
        elif(d2==5):
            print('''
             ________
            | 🌑  🌑 |
            |   🌑   |
            | 🌑  🌑 |
            |________|
        ''')
        elif(d2==6):
            print('''
                         ________
                        | 🌑  🌑 |
                        | 🌑  🌑 |
                        | 🌑  🌑 |
                        |________|
        ''')

        if(d1+d2 == 7 or d1+d2 == 11):
            score += d1+d2
            print(name," you have won the game...")
            print("And your final score is ",score)
            break
        elif(d1+d2 == 2 or d1+d2 == 3 or d1+d2 == 12):
            print(name," oops you have lost the game...")
            print("And your final score is ",score)
            break
        else:
            score += d1+d2
            print(name," your score is ",score)

        play = input("press any key to roll the dice: ")
    x = input("do you want to continue (yes/no): ")


        
    
