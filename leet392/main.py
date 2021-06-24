# LeetCode 392 - Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i = i + 1
                j = j + 1
            else:
                j = j + 1

        return (i >= len(s))

if __name__ == "__main__":
    s1 = "aexe"
    t1 = "abcedxce"

    soln = Solution()
    result = soln.isSubsequence(s1, t1)
    print(result)