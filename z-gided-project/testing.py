import time
import math
import random



start_time = time.time()

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    # v = math.factorial(v)
    # v //= (x + y)
    # v %= 982451653

    return v

print(slowfun_too_slow(2, 5))
z = math.factorial(5)
print(z)
z //= (2+5)
print(z)
z %= 982451653
print(z)



time_interval = time.time() - start_time
print(start_time)
print(time_interval)