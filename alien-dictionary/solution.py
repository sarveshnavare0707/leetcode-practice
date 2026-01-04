'''
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.
'''

class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        mapping = {}
        flag = 0
        for index, charac in enumerate(order):
            mapping[charac] = index
        firstword = [mapping[w] for w in words[0]]
        print(firstword)
        for word in words[1:]:
            nextword = [mapping[w] for w in word]
            print(nextword)
            if firstword>nextword:
                flag =1
            firstword = nextword
        if flag==0:
            return True
        else:
            return False

if __name__ == "__main__":
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    
    solution = Solution()
    result = solution.isAlienSorted(words, order)
    print(result)  # Output: True
