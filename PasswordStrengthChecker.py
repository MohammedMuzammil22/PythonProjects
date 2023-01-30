import getpass

def sugession(lower_w,upper_w,digit,spl_w):
    if(lower_w==0):
        print("*lower character*")
    if(upper_w==0):
        print("*upper character*")
    if(digit==0):
        print("*digit*")
    if(spl_w==0):
        print("*special character*")

def P_S_C():
    lower_w=upper_w=digit=spl_w=score = 0
    note=""
    x=input('''.......Welcome to password strength checker.......
Do you want to check your password strength (yes/no): ''')
    print("Your password Must contain atleast '8 characters' in which atleast '1 Upper case','1 special character' and '1 digit'")
    password = getpass.getpass("Enter your Password: ")
    while(len(password)<8):
        print("Your password Must contain atleast 8 characters")
        password = getpass.getpass("Enter your Password: ")
    for i in password:
        if(i.islower()):
            lower_w += 1
        elif(i.isupper()):
            upper_w += 1
        elif(i.isdigit()):
            digit += 1
        else:
            spl_w += 1

    if(lower_w>=1):
        score += 1
    if(upper_w>=1):
        score += 1
    if(digit>=1):
        score += 1
    if(spl_w>=1):
        score += 1

    if(score == 1):
        note = "That\'s a very bad password.Change it as soon as possible."
    if(score == 2):
        note = 'Your password is okay, but it can be improved.'
    if(score == 3):
        note = 'Your password is hard to guess. But you could make it even more secure.'        
    if(score == 4):
        note = 'Now that\'s one hell of a strong password!!! Hackers don\'t have a chance guessing that password!'

    print("__________________________Password attributes__________________________")
    print(f"The no. of lower character in your password is: {lower_w}")
    print(f"The no. of upper character in your password is: {upper_w}")
    print(f"The no. of digit in your password is: {digit}")
    print(f"The no. of special character in your password is: {spl_w}")
    print("__________________________Password Strength__________________________")
    print("Your password Strength is : ",(score/4))
    print(note)
    if(score<=3):
        print("__________________________Sugession__________________________")
        print("Sugession: To improve your password try to include: ")
        sugession(lower_w,upper_w,digit,spl_w)

x=""
while(x.lower()!="no"):
    P_S_C()
    x = input("do you want to check check password strength again (yes/no): ")