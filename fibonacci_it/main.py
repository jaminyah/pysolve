def fib(n: int) -> int:
    fibseq = [0, 1]

    i = 2
    while i <= n:
        fibnum = fibseq[i - 1] + fibseq[i - 2]
        fibseq.append(fibnum)
        i = i + 1
    
    lastIndex = len(fibseq) - 1
    return fibseq[lastIndex]

if __name__ == "__main__":

    print(fib(6))