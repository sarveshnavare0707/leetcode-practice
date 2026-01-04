'''
The array-form of an integer num is an array representing its digits in left to right order.

    For example, for num = 1321, the array form is [1,3,2,1].

Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
'''

class Solution:
    def addToArrayForm(self, num, k: int):
        total = 0
        for n in num:
            total = (total*10) + n
        newtotal = total+k
        newnum = []
        while newtotal>0:
            r = newtotal%10
            newnum.append(r)
            newtotal = newtotal//10
        return newnum[::-1]
    
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