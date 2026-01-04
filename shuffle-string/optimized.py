'''
You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.
'''

class Solution:
    def restoreString(self, s: str, indices) -> str:
        s = list(s)
        for i in range(len(indices)):
            while indices[i] != i:
                target_idx = indices[i]
                s[i], s[target_idx] = s[target_idx], s[i]
                indices[i], indices[target_idx] = indices[target_idx], indices[i]
        return ''.join(s)
    
if __name__ == "__main__":
    s = "codeleet"
    indices = [4,5,6,7,0,2,1,3]
    print(Solution().restoreString(s, indices)) # "leetcode"
    s = "abc"
    indices = [0,1,2]
    print(Solution().restoreString(s, indices)) # "abc"
    s = "aiohn"
    indices = [3,1,4,2,0]
    print(Solution().restoreString(s, indices)) # "nihao"
