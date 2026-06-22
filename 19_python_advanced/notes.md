# Python Threading Notes

## What is Threading?

A thread is the smallest unit of execution within a process.

Normally, Python executes statements sequentially:

```python
task1()
task2()
```

Threading allows multiple tasks to run concurrently:

```python
Thread(target=task1)
Thread(target=task2)
```

This is useful when tasks spend time waiting, such as:

* Network requests
* File I/O
* Database operations
* Sleep operations

---

## Process vs Thread

| Process                    | Thread                |
| -------------------------- | --------------------- |
| Independent execution unit | Part of a process     |
| Has its own memory         | Shares process memory |
| More expensive to create   | Lightweight           |
| Better isolation           | Faster communication  |

Example:

Browser Process

* Thread 1: UI
* Thread 2: Network
* Thread 3: Rendering

---

# Creating a Thread

```python
import threading

def greet():
    print("Hello")

t = threading.Thread(target=greet)
t.start()
t.join()
```

### Explanation

* `Thread()` → Creates a thread object.
* `target` → Function to execute.
* `start()` → Starts thread execution.
* `join()` → Waits for thread completion.

---

# start()

```python
t.start()
```

Starts a new thread and executes the target function.

Without `start()`, the thread will never run.

---

# join()

```python
t.join()
```

Makes the main thread wait until the child thread finishes.

Example:

```python
t.start()
t.join()

print("Completed")
```

Output:

```text
Hello
Completed
```

---

# Passing Arguments to Threads

```python
def display(name):
    print(name)

t = threading.Thread(
    target=display,
    args=("Deepthi",)
)

t.start()
```

### Important

For a single argument:

```python
args=("Deepthi",)
```

The comma is mandatory.

---

# Multiple Threads Example

```python
t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)

t1.start()
t2.start()

t1.join()
t2.join()
```

### Complexity

If both functions perform constant work:

Time Complexity: O(1)

Space Complexity: O(1)

---

# ThreadPoolExecutor

Instead of manually creating many threads, Python provides a thread pool.

```python
from concurrent.futures import ThreadPoolExecutor
```

Benefits:

* Easier management
* Reuses threads
* Cleaner code
* Better scalability

---

# submit()

Executes a single task.

```python
from concurrent.futures import ThreadPoolExecutor

def add(x, y):
    return x + y

with ThreadPoolExecutor(max_workers=2) as executor:
    future = executor.submit(add, 3, 4)

print(future.result())
```

Output:

```text
7
```

### Complexity

Time Complexity: O(1)

Space Complexity: O(1)

---

# map()

Executes a function on multiple inputs.

```python
from concurrent.futures import ThreadPoolExecutor

def square(x):
    return x*x

nums = [1,2,3,4]

with ThreadPoolExecutor(max_workers=2) as executor:
    result = executor.map(square, nums)

print(list(result))
```

Output:

```text
[1, 4, 9, 16]
```

### Complexity

Let n = number of inputs

Time Complexity: O(n)

Space Complexity: O(n)

---

# submit() vs map()

| submit()                        | map()                        |
| ------------------------------- | ---------------------------- |
| Single task                     | Multiple tasks               |
| Returns Future object           | Returns iterator             |
| More control                    | Simpler                      |
| Can execute different functions | Same function on many inputs |

---

# Future Object

A Future represents a result that will be available later.

```python
future = executor.submit(add, 3, 4)
```

Retrieve result:

```python
future.result()
```

---

# Threading Use Cases

Useful for:

* Downloading files
* API calls
* Web scraping
* File reading/writing
* Database operations

Not ideal for:

* Heavy CPU calculations
* Large mathematical computations

For CPU-intensive tasks use:

```python
multiprocessing
```

instead of threading.

---

# Python GIL (Important Question)

GIL = Global Interpreter Lock

In CPython:

* Only one thread executes Python bytecode at a time.
* Multiple threads help with I/O-bound tasks.
* Multiple threads do not significantly speed up CPU-bound tasks.

 Answer:

"Threading is beneficial for I/O-bound tasks, while multiprocessing is preferred for CPU-bound tasks because of Python's GIL."

---

# Common  Questions

### What is a thread?

A lightweight unit of execution within a process.

---

### Difference between start() and run()?

`start()`

* Creates a new thread.
* Calls `run()` internally.

`run()`

* Executes in the current thread.

---

### Why use join()?

To wait for thread completion.

---

### What is ThreadPoolExecutor?

A high-level API for managing a pool of worker threads.

---

### What does submit() return?

A Future object.

---

### What does map() return?

An iterator containing results.

---

# Complexity Summary

| Operation     | Time | Space |
| ------------- | ---- | ----- |
| Create Thread | O(1) | O(1)  |
| start()       | O(1) | O(1)  |
| join()        | O(1) | O(1)  |
| submit()      | O(1) | O(1)  |
| map()         | O(n) | O(n)  |

---

# Revision Checklist

* [ ] What is a thread?
* [ ] Process vs Thread
* [ ] start()
* [ ] join()
* [ ] args parameter
* [ ] ThreadPoolExecutor
* [ ] submit()
* [ ] map()
* [ ] Future object
* [ ] GIL
* [ ] I/O-bound vs CPU-bound
