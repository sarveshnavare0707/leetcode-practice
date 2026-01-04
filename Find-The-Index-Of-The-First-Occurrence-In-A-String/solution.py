'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        arr = haystack.split(needle)
        print(arr)
        if len(arr)<2:
            return -1
        elif haystack==needle:
            return index
        else:
            l = len(needle)
            while(index<=len(haystack)-l):
                if haystack[index:index+l]==needle:
                    return index
                else:
                    index = index+1

if __name__ == "__main__":
    haystack = "sadbutsad"
    needle = "sad"
    sol = Solution()
    print(sol.strStr(haystack, needle))  # Output: 0
    haystack = "leetcode"
    needle = "leeto"
    print(sol.strStr(haystack, needle))  # Output: -1
    haystack = "hello"
    needle = "ll"
    print(sol.strStr(haystack, needle))  # Output: 2