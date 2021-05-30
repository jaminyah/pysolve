def solution (A: list, K: int):

    for count in range(K):
        temp = A[len(A) - 1]
        for index in range(len(A)):
            A[len(A) - (index + 1)] = A[len(A) - (index + 2)]
        A[0] = temp
    
    for index in range(len(A)):
        print(A[index])

if __name__ == '__main__':
    A1 = [6, 3, 8, 9, 7, 11, 13]
    solution(A1, 3)