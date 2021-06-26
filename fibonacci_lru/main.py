# Reference: 
# https://stackoverflow.com/questions/61604632/fibonacci-function-memoization-in-python

from functools import lru_cache

@lru_cache
def fib(n):
    if n in {0, 1}:
        return n
    
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    print(fib(300))