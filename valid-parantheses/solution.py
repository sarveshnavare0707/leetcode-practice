'''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.
'''

# smart way
class Solution1:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''

# stack way    
class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {"}":"{",")":"(","]":"["}
        for item in s:
            if stack and stack[-1]==map.get(item):
                stack.pop()
            else:
                stack.append(item)
        if len(stack)==0:
            return True
        else:
            return False

# Example usage:
if __name__ == "__main__":
    sol1 = Solution1()
    print(sol1.isValid("()"))  # Output: True
    print(sol1.isValid("()[]{}"))  # Output: True
    print(sol1.isValid("(]"))  # Output: False
    print(sol1.isValid("([)]"))  # Output: False
    print(sol1.isValid("{[]}"))  # Output: True
    print(sol1.isValid("["))  # Output: False
    print(sol1.isValid("]"))  # Output: False

    sol2 = Solution2()
    print(sol2.isValid("()"))  # Output: True
    print(sol2.isValid("()[]{}"))  # Output: True
    print(sol2.isValid("(]"))  # Output: False
    print(sol2.isValid("([)]"))  # Output: False
    print(sol2.isValid("{[]}"))  # Output: True
    print(sol2.isValid("["))  # Output: False
    print(sol2.isValid("]"))  # Output: False

