stack=[]
def push(x):
    stack.append(x)

def pop():
    if not isempty():
        return stack.pop()
    else:
        return "Stack is empty"

def size():
    return len(stack)

def isempty():
    if len(stack)==0:
        return True
    else:
        return False
def peek():
    if not isempty():
        return stack[-1]
    else:
        return "Stack is empty"
def display():
    if not isempty():
        print(stack)
    else:
        print("Stack is empty")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
while(True):

    print("1.push")
    print("2.pop")
    print("3.size")                                                  
    print("4.isempty")
    print("5.peek")
    print("6.display")
    ch=int(input("enter your choice:"))
    if ch==1:
        x=int(input("enter the elemnt to insert"))
        push(x)
    elif ch==2:
        print(pop())
    elif ch==3:
        print(size())
    elif ch==4:
        print(isempty())
    elif ch==5:
        print(peek())
    elif ch==6:
        display()
    else:
        print("invalid choice") 


