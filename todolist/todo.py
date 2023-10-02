class Task:
    def __init__ (self,title,status='incomplete'):
        #init is constructor and stands for initialize
        #self is reference to object of class
        self.title=title
        self.status=status

def add_task(task_name):
    task=Task(task_name)
    with open("task.txt","a")as x:
        x.write(f'{task.title} ({task.status})\n')
        
def view_task():
    with open("task.txt","rt")as x:
        tasks=x.readlines()
        if not tasks:
            print("No tasks found.")
        else:
            for i,task in enumerate(tasks,start=1):
                print(f'{i}.{task.strip()}')
            print('\n')
            
def remove_task(index):
    tasks=[]
    try:
        with open("task.txt",'rt')as y:
            tasks=y.readlines()
            if(index>=1):
                del tasks[index-1]
                with open('task.txt','w')as z:
                    z.writelines(tasks)
                print("task removed successfully")
            else:
                print("invalid task number to remove")
    except FileNotFoundError:
        print("no tasks found")

def mark_complete(index1):
    tasks=[]
    try:
        with open("task.txt",'rt')as y:
            tasks=y.readlines()
            if(index1>=1):
                task_complete=tasks[index1-1].strip()
                task_complete=task_complete.replace('incomplete','complete')
                tasks[index1-1]=task_complete+"\n"
                with open('task.txt','w')as z:
                    z.writelines(tasks)
                print("task marked completed")
    except FileNotFoundError:
        print("no tasks found")
        

def display_menu():
    print("1. add task to list")
    print("2. remove a task from list")
    print("3. mark a task as completed")
    print("4. display to-do list")
    print("5. exit")
    print("\n")

while(True):
    display_menu()
    choice=int(input("make your choice:"))
    if(choice==1):
        task_name=input("enter task name:")
        add_task(task_name)
        print("task added successfully")
    elif(choice==2):
        view_task()
        index=int(input("enter which index task to remove:"))
        remove_task(index)
    elif(choice==3):
        view_task()
        index1=int(input("enter which task to mark complete:"))
        mark_complete(index1)
    elif(choice==4):
        view_task()
    elif(choice==5):
        break