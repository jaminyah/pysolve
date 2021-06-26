# Leetcode: 442

# Method: Add count of each element to a hash table
# Find all keys with values greater than 1
# Add the values to an array. Return the array.

def find_dups(l: list) -> list:
    dups = []                           # empty list
    hashMap = {}                        # empty dictionary

    # count elements in the list
    for elem in l:
        if elem in hashMap:
            hashMap[elem] += 1          # increment value of key
        else:
            hashMap[elem] = 1           # key not present so add key, set value to 1
    
    # add duplicated elements to array
    for key in hashMap:
        if hashMap[key] > 1:
            dups.append(key)

    return dups

if __name__ == '__main__':
    l1 = ['a', 'b', 'd', 'a', 'c', 'd', 'a', 'c', 'b']
    dupl = find_dups(l1)
    print(dupl)