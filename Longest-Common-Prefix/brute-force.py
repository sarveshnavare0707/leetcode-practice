'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs)==1:
            return strs[0]
        if len(list(set(strs)))==1:
            return list(set(strs))[0]
        lcp = ""
        first = strs[0]
        for i in range(1,len(first)+1):
            sub = first[0:i]
            flag = 0
            for j in range(1,len(strs)):
                if strs[j][0:i]!=sub:
                    flag = 1
            if flag==0:
                lcp = sub
            else:
                return lcp
        return lcp
        
if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
    print(s.longestCommonPrefix(["dog","racecar","car"]))      # Output: ""
    print(s.longestCommonPrefix(["a"]))                        # Output: "a"
    print(s.longestCommonPrefix([""]))                         # Output: ""
    print(s.longestCommonPrefix(["ab", "a"]))                  # Output: "a"