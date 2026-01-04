'''
Given an integer n, return any array containing n unique integers such that they add up to 0.
'''

class Solution:
    def sumZero(self, n: int):
        if n==1:
            return [0]
        else:
            nums = []
            if n%2==0:
                for i in range(1,(n//2)+1):
                    nums.append(i)
                    nums.append(-i)
            else:
                nums.append(0)
                for i in range(1,(n//2)+1):
                    nums.append(i)
                    nums.append(-i)
            return nums
        
if __name__ == "__main__":
    s = Solution()
    print(s.sumZero(5))  # Output: [0, 1, -1, 2, -2]
    print(s.sumZero(4))  # Output: [1, -1, 2, -2]
    print(s.sumZero(3))  # Output: [0, 1, -1]
    print(s.sumZero(1))  # Output: [0]