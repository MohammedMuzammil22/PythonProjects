import pickle

def ToDoList():
    to_do_list = []
    stat = []
    try:
        with open("todolist.pkl", "rb") as file:
            to_do_list = pickle.load(file)
        with open("todo_stat.pkl","rb") as file:
            stat = pickle.load(file)
    except:
        pass

    x = input("Do you want to create a ToDOList (yes/no): ")
    name = input("Enter your name :")
    while(x.lower()!="no"):
        choice = int(input('''1.Add a ToDo
2.Edit
3.Delete
4.display all ToDos
5.clear all ToDo's
6.Edit ToDo status
7.Exit
select choice: '''))
        if(choice==1):
            add = input("Add a ToDo :")
            to_do_list.append(add)
            stat.append("x")
            display(to_do_list,name,stat)
        elif(choice==2):
            index = int(input("Enter the index of ToDo to be edited: "))
            editedToDo =  input("Enter the new ToDo: ")
            to_do_list[index-1]= editedToDo
            display(to_do_list,name,stat)
        elif(choice==3):
            index = int(input("Enter the index of ToDo to be deleted: "))
            to_do_list.pop((index-1))
            stat.pop(index-1)
            display(to_do_list,name,stat)

        elif(choice==4):
            if((len(to_do_list))==0):
                print("Your ToDo is empty add items to display them")
            else:    
                display(to_do_list,name,stat)
        elif(choice==5):
            to_do_list.clear()
            stat.clear()
            display(to_do_list,name,stat)
            print("Your ToDo is empty add ToDo's to display: ")
        elif(choice==6):
            index = int(input("Enter the index of the task which is completed : "))
            stat[index-1]="Done"
            display2(to_do_list,name,index,stat)

        else:
            break

    with open("todolist.pkl","wb") as file:
        pickle.dump(to_do_list,file)
    with open("todo_stat.pkl","wb") as file:
        pickle.dump(stat,file)
        
def display(to_do_list,name,stat):
    
    print(f"_____{name}'s ToDo's_____ ")
    for i in range(len(to_do_list)):
        print(i+1,"",to_do_list[i],f" -->  {stat[i]}")
    print("_____________________________")

def display2(to_do_list,name,index,stat):
    
    print(f"_______{name}'s ToDo's_______ ")
    for i in range(len(to_do_list)):
        if(index-1==i):
            print(i+1,"",to_do_list[i],f" -->  {stat[index-1]}")
        else:
            print(i+1,"",to_do_list[i],f" -->   {stat[i]}")
    print("_____________________________")
    
ToDoList()