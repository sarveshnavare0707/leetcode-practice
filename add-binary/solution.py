'''
Given two binary strings a and b, return their sum as a binary string.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        suma = 0
        sumb = 0
        lena = len(a)
        lenb = len(b)
        for a1 in a:
            suma = suma + (2 ** (lena-1)) * int(a1)
            lena -= 1     
        for b1 in b:
            sumb = sumb + (2 ** (lenb-1)) * int(b1)
            lenb -= 1      
        ans = suma + sumb
        res = ""
        if ans>0:
            while ans>0:
                if ans%2==0:
                    res = res + "0"
                else:
                    res = res + "1"
                ans = ans//2
            return res[::-1]
        else:
            return "0"
        
if __name__ == "__main__":
    a = "1010"
    b = "1011"
    
    solution = Solution()
    result = solution.addBinary(a, b)
    print(result)  # Output: "10101"