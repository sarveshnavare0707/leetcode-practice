'''
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.
'''

class Solution:
    
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def f(date):
            y, m, d = map(int, date.split('-'))
            if m < 3:
                m += 12
                y -= 1
            return 365 * y + y // 4 + y // 400 - y // 100 + d + (153 * m + 8) // 5
        
        return abs(f(date1) - f(date2))

if __name__ == "__main__":
    date1 = "2020-01-15"
    date2 = "2019-12-31"
    print(Solution().daysBetweenDates(date1, date2))  # Output: 15
    date1 = "2020-01-01"
    date2 = "2019-12-31"
    print(Solution().daysBetweenDates(date1, date2))  # Output: 1