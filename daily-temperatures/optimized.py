'''
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.
'''

class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0] * len(temperatures)
        stack = [] # tuple stack

        for i,t in enumerate(temperatures):
            while stack and stack[-1][0]<t:
                temp,index = stack.pop()
                result[index] = i-index
            stack.append((t,i))
        return result
    
if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures([73,74,75,71,69,72,76,73])) # Output: [1,1,4,2,1,1,0,0]
    print(s.dailyTemperatures([30,40,50,60])) # Output: [1,1,1,0]
    print(s.dailyTemperatures([90,60,30])) # Output: [0,0,0]