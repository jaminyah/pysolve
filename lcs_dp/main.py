'''
 Reference:
    https://www.algotree.org/algorithms/dynamic_programming/longest_common_subsequence/
 ''' 

from typing import List

def lcs_dp(a:List[str], b: List[str]) -> (int, str):

    rows = len(a)
    cols = len(b)
    count = 0

    # 2D table initialized with zeros
    table = [0] * (rows + 1)        # or table = [ [-1] * (rows + 1) for i in range(cols + 1)]
    for k in range(rows + 1):
        table[k] = [0] * (cols + 1) 

    for i in range(rows + 1):
        for j in range(cols + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1]
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    
    count = table[rows][cols]        # last position in table will accumulate count
    # return count
    
    # build lcs of chars
    i = rows
    j = cols
    substr = ""

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            substr = substr + a[i - 1]
            i = i - 1
            j = j - 1
        elif table[i - 1][j] > table[i][j - 1]:
            i = i - 1
        else:
            j = j - 1
    
    chars =  list(reversed(substr))       # or substr[::-1]
    s = ""
    s = s.join(chars)
    return (count, s)

if __name__ == '__main__':
    seq = ["agort", "bgpoat"]

    result = lcs_dp(seq[0], seq[1])
    print(f"result: {result}")