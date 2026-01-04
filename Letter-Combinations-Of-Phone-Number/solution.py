'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

class Solution:
    def letterCombinations(self, digits: str):

        if digits=="":
            return []

        def cart_prod(aa1,aa2):
            newaa = []
            for a1 in aa1:
                for a2 in aa2:
                    newaa.append(a1+a2)
            return newaa

        mapping = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        aa = []
        for d in digits:
            aa.append(mapping.get(d))
        item1 = aa[0]
        for i in range(1,len(aa)):
            item1 = cart_prod(item1,aa[i])
        return item1

if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(s.letterCombinations(""))     # Output: []
    print(s.letterCombinations("2"))    # Output: ["a","b","c"]
    print(s.letterCombinations("7"))    # Output: ["p","q","r","s"]
    print(s.letterCombinations("234"))  # Output: ["adg", "adh", "adi", "aeg", "aeh", "aei", ...]