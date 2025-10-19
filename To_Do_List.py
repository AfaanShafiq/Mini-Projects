Tasks = []
def To_Do():
    while(True):
        print("!-----------------------!")
        print("To Do List\n1. Add new Task \n2. View Tasks \n3. Delete Task \n4. Close")
        print("!-----------------------!")
        try:
            value = int(input("What would you like to do: "))
        except ValueError:
            print("Enter Valid Number")
            continue
        if(0< value <=4):
            if(value == 1):
                Add()
            elif(value==2):
                View()
            elif(value==3):
                Delete()
            elif(value==4):
                print("To Do List Closed")
                break
        else:
            print("Enter Valid Number")
def Add():
    while(True):
        task = input("Enter Task: ")
        Tasks.append(task)
        print("Task Added!")
        new = input("Add another task? yes/no: ").lower()
        if(new == "no"):
            break
        elif(new == "yes"):
            continue
        else:
            print("Enter Valid Input")
            break


def View():
    i = 1
    for el in Tasks:
        print(f"{i}.",el) 
        i+=1
    print("\n")
    return

def Delete():
    print("Which Task do you want to delete?")
    View()
    while(True):
        if(len(Tasks)==0):
            print("No Tasks")
            return
        else:
            try:
                num = int(input("Enter Task Number: "))
            except ValueError:
                print("Enter Valid Number")
                return
            if(0 < num <=len(Tasks)):
                Tasks.pop(num-1)
                print("Task Deleted")
                return
            else:
                print("Enter Valid Number")
                continue

To_Do()


