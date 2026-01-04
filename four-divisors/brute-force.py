# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

 

# Example 1:

# Input: nums = [21,4,7]
# Output: 32
# Explanation: 
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.

# Example 2:

# Input: nums = [21,21]
# Output: 64

# Example 3:

# Input: nums = [1,2,3,4,5]
# Output: 0


# class Solution:
#     def sumFourDivisors(self, nums: List[int]) -> int:
#         def divisors(n):
#             divs = []
#             for i in range(1,n+1):
#                 if n%i==0:
#                     divs.append(i)
#             return divs
#         total = 0
#         for n in nums:
#             divs = divisors(n)
#             if len(divs)==4:
#                 total=total+sum(divs)
#         return total

import math
from typing import List
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divisors(n):
            divs = []
            m = math.isqrt(n)
            for i in range(1,m+1):
                if n%i==0:
                    j = n//i
                    divs.append(i)
                    if j!=i:
                        divs.append(j)
            return divs
        total = 0
        for n in nums:
            divs = divisors(n)
            print(divs)
            if len(divs)==4:
                total=total+sum(divs)
        return total