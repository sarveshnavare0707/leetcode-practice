'''
You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.
'''

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1,n+1):
            if n%i==0:
                factors.append(i)
        if len(factors)<k:
            return -1
        else:
            return factors[k-1]
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.kthFactor(12, 3))  # Output: 3
    print(sol.kthFactor(7, 2))   # Output: 7
    print(sol.kthFactor(4, 4))   # Output: -1
    print(sol.kthFactor(1, 1))   # Output: 1
    print(sol.kthFactor(10, 5))  # Output: -1