'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        for i in s:
            if stack1 and i=='#':
                stack1.pop()
            elif i=='#':
                continue
            else:
                stack1.append(i)
        stack2 = []
        for j in t:
            if stack2 and j=='#':
                stack2.pop()
            elif j=='#':
                continue
            else:
                stack2.append(j)
        if stack1==stack2:
            return True
        else:
            return False
        
if __name__ == "__main__":
    s = "ab#c"
    t = "ad#c"
    sol = Solution()
    print(sol.backspaceCompare(s, t))  # Output: True
    s = "ab##"
    t = "c#d#"
    print(sol.backspaceCompare(s, t))  # Output: True
    s = "a##c"
    t = "#a#c"
    print(sol.backspaceCompare(s, t))  # Output: True
    s = "a#c"
    t = "b"
    print(sol.backspaceCompare(s, t))  # Output: False