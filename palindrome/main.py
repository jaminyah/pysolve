def isPalindrome(input: str) -> bool:
    reversed = input[::-1]
    if input == reversed:
        return True
    else:
        return False

if __name__ == '__main__':

    num = 12212
    num_str = str(num)
    result = isPalindrome(num_str)
    print(result)