def isPalindrome(string) -> bool:
    i = 0
    j = len(string) - 1
    input = string.lower()

    while (i <= j):
        if input[i] == input[j]:
            i = i + 1
            j = j - 1
        else:
            return False
    return True