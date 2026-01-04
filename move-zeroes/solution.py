'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        n = 0
        if nums==[0]:
            pass
        else:
            while n<length:
                if nums[n]==0:
                    nums[n:] = nums[n+1:]
                    length=length-1
                    n=n-1
                    nums.append(0)
                n=n+1
            
if __name__ == "__main__":
    nums = [0,1,0,3,12]
    
    solution = Solution()
    solution.moveZeroes(nums)
    print(nums)  # Output: [1, 3, 12, 0, 0]