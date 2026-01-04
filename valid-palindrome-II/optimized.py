'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:

        def verify(left,right,deleted):
            while left<right:
                if s[left]!=s[right]:
                    if deleted:
                        return False
                    else:
                        return verify(left+1,right,True) or verify(left,right-1,True)
                else:
                    left +=1
                    right -=1
            return True
        return verify(0,len(s)-1,False)      

if __name__ == "__main__":
    s = "abca"
    
    solution = Solution()
    result = solution.validPalindrome(s)
    print(result)  # Output: True  