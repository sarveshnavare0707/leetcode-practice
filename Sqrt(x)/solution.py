'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

'''

class Solution:
    def mySqrt(self, x: int) -> int:
        store = []
        if x==0:
            return 0
        else:
            low = 0
            high = x
            while(round(low,8)<round(high,8)):
                mid = (high+low)/2
                if mid*mid>x:
                    high = mid
                    continue
                elif mid*mid<x:
                    store.append(mid)
                    low = mid
                    continue
                else:
                    return int(mid)
            best = int(max(store)//1)
            bestnext = best+1
            if bestnext*bestnext==x:
                return bestnext
            else:
                return best

if __name__ == "__main__":
    x = 4
    sol = Solution()
    print(sol.mySqrt(x))  # Output: 2
    x = 8
    print(sol.mySqrt(x))  # Output: 2
    x = 0
    print(sol.mySqrt(x))  # Output: 0
    x = 3
    print(sol.mySqrt(x)) # Output: 1