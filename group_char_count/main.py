from typing import List

"""
Return a list of chars with similar count in group.
Example: "This is the python way"
Returns {1: ['T', 'e', 'p', 'o', 'n', 'w', 'a'], 3: ['h'], 2: ['i', 's', 't', 'y']}
"""

def groupCounts(array: List[str]) -> dict:
    hashMap = {}

    array = array.replace(" ", "")                      # remove all empty space

    # add count of each char to a hash map
    for key in array:
        hashMap[key] = hashMap.get(key, 0) + 1          # if key not present set value = 0, then add 1

    #print(str(hashMap))

    # group chars based on count 
    group = {}
    for key, value in hashMap.items():
        if value not in group:
            group[value] = [key]
        else:
            group[value].append(key)

    return group

if __name__ == '__main__':
    sentence = "This is the python way"

    result = groupCounts(sentence)
    print(result)