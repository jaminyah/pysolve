def fib(n, memo):
    if memo[n - 1] != 0:
        return memo[n - 1]
    if n == 1 or n == 2:
        return 1
    else:
        result = fib((n - 1), memo) + fib((n -2), memo)
        memo[n - 1] = result
        return result

if __name__ == "__main__":
    memo = [0] * 7
    print(fib(7, memo))