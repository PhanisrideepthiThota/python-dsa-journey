import concurrent.futures
def multiply(x):
    return 2*x
l=[10,20,30,40]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as e:
    res=e.map(multiply,l)
    print(list(res))
    
#Time Complexity: O(n)
# Space Complexity: O(n)
'''
map()
    ↓
gives many tokens/results
    ↓
list(...)
    ↓
gives all answers
'''
