'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapping = {}
        for idx,val in enumerate(s):
            if val in mapping:
                mapping[val].append(idx)
            else:
                mapping[val] = [idx]
        for k,v in mapping.items():
            if len(v)<2:
                return v[0]
        return -1
    
if __name__ == "__main__":
    s = "leetcode"
    sol = Solution()
    print(sol.firstUniqChar(s))  # Output: 0
    s = "loveleetcode"
    print(sol.firstUniqChar(s))  # Output: 2
    s = "aabb"
    print(sol.firstUniqChar(s)) # Output: -1