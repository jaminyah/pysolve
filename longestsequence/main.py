# Match the longest continuous sequence of characters
# that is common to both strings.
# Case 1:
# s1 = "abbcd"
# s2 = "cdea"
# longest continuous sequence common to s1 and s2 is "cd"

# Case 2:
#s1 = "abc"
#s2 = "ac"
# longest continuous sequence common to s1 and s2 is "a" or "c"

# Case 3:
# s1 = "abcdddefgil"
# s2 = "abbdddefghl"
# longest continuous sequence common to s1 and s2 is "dddefg"

def longestsequence(str1: str, str2: str) -> int:
    
    i, j = 0, 0                     # string index
    len1 = len(str1)
    len2 = len(str2)
    longest = 0
    ls = []                         # longest sequence so far

    while i < len1:
        while j < len2:
            if str1[i] == str2[j]:
                ls.append(s1[i])
                if len(ls) > longest:
                    longest = len(ls)
 
                i = i + 1
                j = j + 1
                if i >= len1:
                    break
                else:
                    continue
            else:
                ls = []
                j = j + 1
        i = i + 1
        j = 0
    
    return longest

if __name__ == '__main__':

    #s1 = "abbcd"
    #s2 = "cdea"
    #s1 = "abc"
    #s2 = "ac"
    s1 = "abcdddefgil"
    s2 = "abbdddefghl"
    print(f"length: {longestsequence(s1, s2)}")