'''
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def helper(n):
            if n<5:
                return 0
            return n//5 + helper(n//5)
        return helper(n)

if __name__ == "__main__":
    sol = Solution()
    print(sol.trailingZeroes(5))  # Output: 1
    print(sol.trailingZeroes(10)) # Output: 2
    print(sol.trailingZeroes(25)) # Output: 6
    print(sol.trailingZeroes(100)) # Output: 24
    print(sol.trailingZeroes(0))   # Output: 0