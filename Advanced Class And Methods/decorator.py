import math
import time

def timer(func):
    print('we are ready')
    def inner(*arg,**kargs):
        print('Time Start')
        start = time.time()
        func(*arg,**kargs)
        end=time.time()
        print(f'total time {end-start}')
    return inner

@timer
def get_factorial(n):
    result=math.factorial(n)
    print(f'factorial of{n}is {result}')
get_factorial(923221)
# timer(get_factorial)()

