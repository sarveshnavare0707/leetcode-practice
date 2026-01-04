'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''

class Solution:
    def sortedSquares(self, nums):
        newarray = []
        left = 0
        right = len(nums)
        idx = 0
        for n in range(0,len(nums)):
            if nums[n]<0:
                continue
            else:
                idx = n
                break
        if idx==0 and nums[idx]<0:
            idx=len(nums)-1
        else:
            if abs(nums[idx])>abs(nums[idx-1]):
                idx = idx-1
        newarray.append(nums[idx]**2)
        l = idx-1
        r = idx+1
        while l>=left and r<right:
            l1 = nums[l]**2
            r1 = nums[r]**2
            if l1>r1:
                newarray.append(r1)
                r = r+1
            else:
                newarray.append(l1)
                l = l-1
        if l>=left:
            for i in range(l,-1,-1):
                newarray.append(nums[i]**2)
        if r<right:
            for j in range(r,len(nums)):
                newarray.append(nums[j]**2)
        return newarray
    
# better solution
class Solution2:
    def sortedSquares(self, nums):
        length = len(nums)
        left = 0
        right = length - 1
        ret = [0]*length

        for i in range(length-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                square = nums[left]
                left +=1
            else:
                square = nums[right]
                right -=1
            ret[i] = square*square

        return ret
    
if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    solution = Solution()
    print(solution.sortedSquares(nums))  # Output: [0, 1, 9, 16, 100]
    
    solution2 = Solution2()
    print(solution2.sortedSquares(nums))  # Output: [0, 1, 9, 16, 100]
