'''
Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.
'''

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        factors1 = []
        factors2 = []
        for i in range(1,a+1):
            if a%i==0:
                factors1.append(i)
        for j in range(1,b+1):
            if b%j==0:
                factors2.append(j)
        return len(set(factors1)&set(factors2))
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.commonFactors(12, 6))  # Output: 4
    print(sol.commonFactors(25, 30)) # Output: 2
    print(sol.commonFactors(8, 12))  # Output: 4
    print(sol.commonFactors(7, 14))  # Output: 2
    print(sol.commonFactors(1, 1))   # Output: 1