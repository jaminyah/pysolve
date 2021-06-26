# Ref: 
# https://stackoverflow.com/questions/61604632/fibonacci-function-memoization-in-python

cache = {0: 0, 1: 1}

def fib(n):
    if n in cache:
        return cache[n]
    
    # recurse to max 100 levels
    for i in range(100, n, 100):
        fib(i)
    
    cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]

if __name__ == "__main__":
  
    result = fib(300)
    print(result)
