'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.
'''

class Solution:
    def isMonotonic(self, nums) -> bool:
        if nums[0]-nums[-1]>0:
            for i in range(0,len(nums)-1):
                if nums[i]<nums[i+1]:
                    return False
        elif nums[0]-nums[-1]<0:
            for i in range(0,len(nums)-1):
                if nums[i]>nums[i+1]:
                    return False
        else:
            if len(set(nums))!=1:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isMonotonic([1, 2, 2, 3]))  # Output: True
    print(sol.isMonotonic([6, 5, 4, 4]))  # Output: True
    print(sol.isMonotonic([1, 3, 2]))     # Output: False
    print(sol.isMonotonic([1, 2, 4, 5]))  # Output: True