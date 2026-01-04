'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        badversions = []
        while (high!=low):
            mid = low + (high-low)//2
            if isBadVersion(mid): #leetcode defines this function
                high = mid
                badversions.append(mid)
            else:
                low = mid+1
        if badversions:
            return min(badversions)
        else:
            return n
        
if __name__ == "__main__":
    n = 5
    bad = 4
    
    solution = Solution()
    result = solution.firstBadVersion(n)
    print(result)  # Output: 4