def checkIfPangram(input: str) -> bool:

    # Create a set containing all letters of the alphabet
    u = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'y', 'z'}

    # Create an empty set
    v = set()

    chars = input.lower()
    for char in chars:
        v.add(char)
    
    return u.issubset(v)

if __name__ == '__main__':

    #inputStr = "leetcode"
    inputStr = "The quick brown fox jumps over the lazy dog."
    result = checkIfPangram(inputStr)
    print(f"Pangram: {result}")