import threading
import time

def f1():
    print("Hello")
    time.sleep(1)
    print("Hai")

def f2():
    print("WELCOME")
    time.sleep(1)
    print("BYE BYE!")

t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)
t1.start()
t2.start()
t1.join()
t2.join()

#Time Complexity: O(1)
#Space Complexity: O(1)
