'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
'''

class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        i=0
        if flowerbed==[0]:
            return True
        else:
            while(i<len(flowerbed)-1):
                if i==0 and flowerbed[i+1]==0 and flowerbed[i]==0:
                    n=n-1
                    flowerbed[i]=1
                    i = i + 1
                elif flowerbed[i+1]==0 and flowerbed[i]==0 and flowerbed[i-1]==0:
                    n=n-1
                    flowerbed[i]=1
                    i = i + 1
                elif i==len(flowerbed)-2 and flowerbed[i+1]==0 and flowerbed[i]==0:
                    n=n-1
                    flowerbed[i+1]=1
                    i = i + 1
                else:
                    i=i+1
        if n>0:
            return False
        else:
            return True

if __name__ == "__main__":
    flowerbed = [1,0,0,0,1]
    n = 1
    print(Solution().canPlaceFlowers(flowerbed, n))  # Output: True
    flowerbed = [1,0,0,0,1]
    n = 2
    print(Solution().canPlaceFlowers(flowerbed, n))  # Output: False