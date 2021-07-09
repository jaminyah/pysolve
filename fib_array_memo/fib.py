# Fibonacci - memoize using tabulation method 

def fibonacci(n: int) -> int:
    
    if n <= 1:
        return n
    
    F = []
    for i in range(n + 1):          # initialize from index 0 - index n
        F.append(-1)

    F[0] = 0
    F[1] = 1

    j = 2
    while j < n + 1:                # compute for index 2 - index n
        F[j] = F[j - 2] + F[j - 1]
        j = j + 1

    return F[n]