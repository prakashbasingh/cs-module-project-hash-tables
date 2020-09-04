# Your code here
import math
import random
import time

start_time = time.time()


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

chaching = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    if (x, y) in chaching: # if key and value in chaching return the value
        return chaching[(x, y)]
    else: #if key and value is not in the chaching return following
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
         
        chaching[(x, y)] = v
        
        return chaching[(x, y)]


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

end_time = time.time()
time_interval = end_time - start_time
print(start_time)
print(end_time)
print(time_interval)