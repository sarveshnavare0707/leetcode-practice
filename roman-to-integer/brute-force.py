'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        t = 0
        l = 0
        while(l<=len(s)-1):
            
            if s[l]=='V':
                t = t+5
                l=l+1
                continue
            if s[l]=='L':
                t = t+50
                l=l+1
                continue
            if s[l]=='D':
                t = t+500
                l=l+1
                continue
            if s[l]=='M':
                t = t+1000
                l=l+1
                continue
    
            if s[l]=='I':
                if l+1<len(s):
                    if s[l+1] == 'V':
                        t = t+4
                        l = l+2
                        continue
                    elif s[l+1]=='X':
                        t = t + 9
                        l = l + 2
                        continue
                    else:
                        t = t+1
                        l = l+1
                        continue
                else:
                    t=t+1
                    l=l+1
                    continue
            
            if s[l]=='X':
                if l+1<len(s):
                    if s[l+1] == 'L':
                        t = t+40
                        l = l+2
                        continue
                    elif s[l+1]=='C':
                        t = t + 90
                        l = l + 2
                        continue
                    else:
                        t = t+10
                        l = l+1
                        continue
                else:
                    t=t+10
                    l=l+1
                    continue
        
            if s[l]=='C':
                if l+1<len(s):
                    if s[l+1] == 'D':
                        t = t+400
                        l = l+2
                        continue
                    elif s[l+1]=='M':
                        t = t + 900
                        l = l + 2
                        continue
                    else:
                        t = t+100
                        l = l+1
                        continue
                else:
                    t=t+100
                    l=l+1
                    continue
        return t

if __name__ == "__main__":
    s = "III"
    print(Solution().romanToInt(s)) # 3
    s = "IV"
    print(Solution().romanToInt(s)) # 4
    s = "IX"
    print(Solution().romanToInt(s)) # 9
    s = "LVIII"
    print(Solution().romanToInt(s)) # 58
    s = "MCMXCIV"
    print(Solution().romanToInt(s)) # 1994