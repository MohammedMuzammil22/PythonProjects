import random
r_no = random.randint(1,100)
name = input("What is your name: ")
i = 1
while(i):
    n = int(input("Guess a no. between 1-100 :"))
    if(n<1 or n>100):
        print("Guess a number within the range 1-100 :")
    elif(n==r_no):
        print('''You have guessed it right
The random is ''',r_no)
        print(name," you have guessed it in ",i," attempts...")
        y = input("Do you want to play again (yes/no) :")
        if(y.lower()=="yes"):
            i=1
            r_no = random.randint(1,100)
        else:
            break
    elif(n<r_no):
        print("Guess a higher number : ")
        i += 1
    else:
        print("Guess a lower number : ")
        i += 1


    
