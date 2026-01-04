'''
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.
'''

class Solution:
    def generateParenthesis(self, n: int):
        result = []

        def backtrack(s,openct,closect):
            
            if len(s)==2*n:
                result.append(s)
            if openct<n:
                backtrack(s+"(",openct+1,closect)
            if closect<openct:
                backtrack(s+")",openct,closect+1)
        
        backtrack("",0,0)

        return result
    
if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3)) # Output: ["((()))","(()())","(())()","()(())","()()()"]
    print(s.generateParenthesis(1)) # Output: ["()"]
    print(s.generateParenthesis(2)) # Output: ["(())","()()"]

# time complexity: O(4^n*sqrt(n)) where n is the number of pairs of parentheses (reference is catalan number) -  not sure its O(4^n/sqrt(n)) as it is including O(n) for building the string.
# space complexity: O(4^n*sqrt(n)) where n is the number of pairs of parentheses (reference is catalan number) + o(n) for the recursion stack

# Catalan number is a sequence of natural numbers that occur in various counting problems, often involving recursive structures. The nth Catalan number can be expressed directly in terms of binomial coefficients:
# C(n) = (2n)! / ((n + 1)! * n!)
# Cn = Cn-1 * 2(2n-1)/(n+1)