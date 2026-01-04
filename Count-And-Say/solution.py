'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

    countAndSay(1) = "1"
    countAndSay(n) is the run-length encoding of countAndSay(n - 1).

Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.
'''

class Solution:
    def countAndSay(self, n: int) -> str:

        def newrle(rle):
            if rle=='1':
                return '11'
            else:
                ct = 1
                currnum = rle[0]
                newrle = ""
                i=1
                while(i<len(rle)):
                    if rle[i]==currnum:
                        ct = ct+1
                    else:
                        newrle = newrle + str(ct) + currnum
                        currnum = rle[i]
                        ct = 1
                    i = i+1
                newrle = newrle + str(ct) + currnum
                return newrle

        rle = '1'
        if n==1:
            return rle
        else:
            i=1
            while(i!=n):
                rle = newrle(rle)
                i+=1
        return rle
        
if __name__ == "__main__":
    n = 4
    sol = Solution()
    print(sol.countAndSay(n))  # Output: "1211"
    n = 5
    print(sol.countAndSay(n))  # Output: "111221"
    n = 6
    print(sol.countAndSay(n))  # Output: "312211"
    n = 7
    print(sol.countAndSay(n))  # Output: "13112221"