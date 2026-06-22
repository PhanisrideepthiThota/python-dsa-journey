import concurrent.futures
def add(x,y):
    return x+y
x=3
y=4
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as e:
    res=e.submit(add,x,y)
    print(res.result())


#Time Complexity: O(1)
#Space Complexity: O(1)

'''
submit()
    ↓
gives one token
    ↓
future.result()
    ↓
gives one answer
'''
