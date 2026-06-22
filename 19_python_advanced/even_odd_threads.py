import threading
import time

def f(name):
    if name == "A":
        for i in range(0, 100, 2):
            print(name,i)
            time.sleep(1)
    else:
        for i in range(1,100,2):
            print(name,i)
            time.sleep(1)


if __name__=="__main__":
    t1 = threading.Thread(target=f, args=("A",))
    t1.start()
    t2 = threading.Thread(target=f, args=("B",))
    t2.start()

    t1.join()
    t2.join()

#Time Complexity: O(n)
# Space Complexity: O(1)
