'''
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.
'''

class Solution:
    def dailyTemperatures(self, temperatures):
        result = []
        for t in range(0,len(temperatures)):
            flag = 0
            for i in range(t+1,len(temperatures)):
                if temperatures[i]>temperatures[t]:
                    result.append(i-t)
                    flag =1
                    break
            if flag==0:
                result.append(0)
        return result
    
if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures([73,74,75,71,69,72,76,73])) # Output: [1,1,4,2,1,1,0,0]
    print(s.dailyTemperatures([30,40,50,60])) # Output: [1,1,1,0]
    print(s.dailyTemperatures([90,60,30])) # Output: [0,0,0]