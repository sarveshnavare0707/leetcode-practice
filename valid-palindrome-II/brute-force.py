'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        else:
            for i in range(len(s)):
                snew = s[:i]+s[i+1:]
                if snew==snew[::-1]:
                    return True
        return False
    
if __name__ == "__main__":
    s = "abca"
    
    solution = Solution()
    result = solution.validPalindrome(s)
    print(result)  # Output: True