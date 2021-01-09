# To-do application CLI
import sys
import datetime
import os.path

def creat_dict():
    count=1
    tempDict={}
    if os.path.isfile('todo.txt'):
        file = open('todo.txt', 'r') 
        for each in file: 
            tempDict[count]=each
            count+=1
        return tempDict
    else:
        return tempDict
def get_date():
    dt_stamp = datetime.datetime.today()
    date=str(dt_stamp.strftime('%Y-%m-%d'))
    return date

def markAsDone(val):
    date=get_date()
    final_str='x '+date+' '+val
    file=open('done.txt','a')
    file.write(final_str)
    file.close()
def report():
    file = open("done.txt","r") 
    Counter = 0
    # Reading from file 
    Con = file.read() 
    CoList = Con.split("\n") 
    for i in CoList: 
        if i: 
            Counter += 1
    file.close()
    myDict=creat_dict()
    pending=len(myDict)
    date=get_date()
    final=date+' ' + 'Pending : '+str(pending)+' '+u'\u2A2F'+ ' Completed : '+str(Counter)+' '+u'\u2714'
    print(final)
    



def complete(task):
    todoDict=creat_dict()
    if int(task)<=len(todoDict) and int(task)!=0:
        val=todoDict[int(task)]
        del todoDict[int(task)]
        with open("todo.txt", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if i != val:
                    f.write(i)
            f.truncate()
        todoDict=creat_dict()   
        n=len(todoDict)
        #calling function for mark done in done.txt
        markAsDone(val)
        print(u'\u2705'+' Marked todo #'+task+" as done.")
    else:
        print('Error: todo #'+task+" does not exist.")

        




def add(s):
    file=open('todo.txt','a')
    file.write(s)
    file.write("\n")
    file.close()
    print(u'\u2714'+" Added todo: "+'"'+s+'"')

def show():
    todoDict=creat_dict()
    n=len(todoDict)
    if n==0:
        print("There are no pending todos!")
        return
    for item in range(len(todoDict)):
        pr='['+str(n)+']'
        print(pr,end=' ')
        print(todoDict[n],end='')
        n=n-1

def delete(task):
    todoDict=creat_dict()
    if int(task)<=len(todoDict) and int(task)!=0:
        val=todoDict[int(task)]
        del todoDict[int(task)]
        with open("todo.txt", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if i != val:
                    f.write(i)
            f.truncate()
        todoDict=creat_dict()   
        print('\u274C'+' Deleted todo #'+task)
    else:
        print('Error: todo #'+task+" does not exist. Nothing deleted.")





def help():
    print('Usage :-')
    print(u'\u2714'+' ./todo add "todo item"  # Add a new todo')
    print(u'\u2714'+' ./todo ls               # Show remaining todos')
    print(u'\u2714'+' ./todo del NUMBER       # Delete a todo')
    print(u'\u2714'+' ./todo done NUMBER      # Complete a todo')
    print(u'\u2714'+' ./todo help             # Show usage')
    print(u'\u2714'+' ./todo report           # Statistics')

def main():
    # command line argument extrector
    command=""
    task=""
    if len(sys.argv)>1:
        command=sys.argv[1]
    if len(sys.argv)>2:
        task=sys.argv[2]
    if command=='help':
        print('\x1b[6;30;42m' + 'Help' + '\x1b[0m'+'....',end='')  
        print()  
        help()
    elif len(command)==0:
        print('\x1b[6;30;43m' + 'Started successfully' + '\x1b[0m'+'....')

        help()
    elif command=='ls':
        show()
    elif command=='add':
        if task!="":
            add(task)
        else:
            print("Error: Missing todo string. Nothing added!")
    elif command=='done':
        if task!="":
            complete(task)
        else:
            print("Error: Missing NUMBER for marking todo as done.")
    elif command=='report':
        report()
    elif command=='del':
        if task!="":
            delete(task)
        else:
            print("Error: Missing NUMBER for deleting todo.")
    

if __name__ == '__main__':
    # green tick
    # print(u'\u2705')
    main()