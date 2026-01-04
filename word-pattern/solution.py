'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter.
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l1 = list(pattern)
        l2 = s.split(" ")
        if len(l1)!=len(l2):
            return False
        else:
            mapping = {}
            for i in range(0,len(l1)):
                if l1[i] not in mapping and l2[i] not in mapping.values():
                    mapping[l1[i]] = l2[i]
            l3 = [mapping.get(x,None) for x in l1]
            if l3==l2:
                return True
            else:
                return False                    

if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat dog"
    s1 = Solution()
    print(s1.wordPattern(pattern,s))
    pattern = "aaaa"
    s = "dog cat cat dog"
    print(s1.wordPattern(pattern,s))
    pattern = "abba"
    s = "dog dog dog dog"
    print(s1.wordPattern(pattern,s))