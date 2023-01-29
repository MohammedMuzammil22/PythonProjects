import random
import time

mobile = ["XIAOMI","SAMSUNG","APPLE","OPPO","LENOVO","NOKIA","LG","ONEPLUS"]
play=""
while(play.lower()!="no"):
    x = random.randint(0,7)
    hangManword = mobile[x]
    print("HangMan word : ","_ "*len(mobile[x]))
    correctlyGuessed = []
    incorrectlyGuessed = []
    WrongGuesses=0
    abc = ""
    inc = 1
    a=1
    while(inc):
        if(abc==hangManword.lower()):
            print("you have won the game...")
            break
        userGuess = input("Guess a single letter: ")
        if(userGuess in correctlyGuessed):
            print(f"You have already guessed '{userGuess}' .")
            userGuess = input("Guess a single letter: ")
        while(len(userGuess)==0 or len(userGuess)>1):
            userGuess = input("Guess a single letter: ")
        if(userGuess in hangManword.lower()):
            correctlyGuessed.append(userGuess)
            
            if(a==1):
                for i in range(len(hangManword.lower())):
                    t = hangManword.lower()[i:i+1]
                    if(t!=userGuess):
                        abc +="_"
                    else:
                        abc += t
                print(abc)
                a+=1
            else:
                for i in range(len(hangManword.lower())):
                    t = hangManword.lower()[i:i+1]
                    if(t!=userGuess and abc[i]=="_" ):
                        abc = list(abc)
                        abc[i] = "_"
                        abc = "".join(abc)
                    else:
                        abc = list(abc)
                        abc[i] = t
                        abc = "".join(abc)
                print(abc)
        else:
            if(userGuess in incorrectlyGuessed):
                print("Incorrect guess: ",incorrectlyGuessed)

            else:
                incorrectlyGuessed.append(userGuess)
                WrongGuesses += 1
                print("Incorrect guess: ",incorrectlyGuessed)

        if(WrongGuesses==1):
            time.sleep(1)
            print('   _____ \n'
                        '  |      \n'
                        '  |      \n'
                        '  |      \n'
                        '  |      \n'
                        '  |      \n'
                        '  |      \n'
                        '__|__\n')
            print(abc)            
            print('guesses remaining: ',5-WrongGuesses)

        elif(WrongGuesses==2):
            time.sleep(1)
            print('   _____ \n'
                '  |     | \n'
                '  |     | \n'
                '  |      \n'
                '  |      \n'
                '  |      \n'
                '  |      \n'
                '__|__\n')
            print(abc)
            print('guesses remaining: ',5-WrongGuesses)

        elif(WrongGuesses==3):
            time.sleep(1)
            print('   _____ \n'
                '  |     | \n'
                '  |     | \n'
                '  |     | \n'
                '  |      \n'
                '  |      \n'
                '  |      \n'
                '__|__\n')
            print(abc)
            print('guesses remaining: ',5-WrongGuesses)

        elif (WrongGuesses==4):
            time.sleep(1)
            print('   _____ \n'
                '  |     | \n'
                '  |     | \n'
                '  |     | \n'
                '  |     O \n'
                '  |      \n'
                '  |      \n'
                '__|__\n')
            print(abc)
            print('guesses remaining: ',5-WrongGuesses)

        elif (WrongGuesses==5):
            time.sleep(1)
            print('   _____ \n'
                '  |     | \n'
                '  |     | \n'
                '  |     | \n'
                '  |     O \n'
                '  |    /|\ \n'
                '  |    / \ \n'
                '__|__\n')
            print(abc)
            print('Wrong guess. You\'ve been hanged!!!\n')
            print(f'The word was: {hangManword.lower()}')
            break
        inc+=1
    play = input("Would you like to continue (yes/no): ")
