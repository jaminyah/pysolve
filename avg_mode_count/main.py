from typing import List

def countChars(array: List[str]) -> tuple:
    hashMap = {}
    modeVal = ""
    modeFreq = 0
    sum = 0
    charCount = 0

    array = array.replace(" ", "")

    for key in array:
        hashMap[key] = hashMap.get(key, 0) + 1  # Key not found, set to 0 and add 1. Otherwise add 1
        sum = sum + hashMap[key]
        charCount = charCount + 1

        if hashMap[key] > modeFreq:
            modeFreq = hashMap[key]
            modeVal = key

    average = sum / charCount
    print("hashMap: " + str(hashMap))
    print(f"modeVal: {modeVal}, modeFreq: {modeFreq}")
    print(f"average: {average}")

    return (modeVal, modeFreq, average)

if __name__ == '__main__':
    chars = "This is Pythoni world!"
    countChars(chars)

