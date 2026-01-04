'''
The array-form of an integer num is an array representing its digits in left to right order.

    For example, for num = 1321, the array form is [1,3,2,1].

Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
'''

class Solution:
    def addToArrayForm(self, num, k: int):
        carry = k
        for i in range(len(num)-1,-1,-1):
            num[i] = num[i]+carry
            if num[i]>=10:
                carry = num[i]//10
                num[i] = num[i]%10
            else:
                carry = 0
        if carry>0:
            num.insert(0,carry)
        while num[0]>=10:
            n = [num[0]//10]
            num[0] = num[0]%10
            n.extend(num)
            num = n
        return num
    
if __name__ == "__main__":
    s = Solution()
    num = [1,2,0,0]
    k = 34
    print(s.addToArrayForm(num, k)) # Output: [1,2,3,4]
    num = [2,7,4]
    k = 181
    print(s.addToArrayForm(num, k)) # Output: [4,5,5]
    num = [2,1,5]
    k = 806
    print(s.addToArrayForm(num, k)) # Output: [1,0,2,1]