'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''

class Solution: #trivial solution
    def sortedSquares(self, nums):
        result=map(lambda x:x**2,nums)
        b=list(result)
        b.sort()
        return b
    
if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    solution = Solution()
    print(solution.sortedSquares(nums))  # Output: [0, 1, 9, 16, 100]