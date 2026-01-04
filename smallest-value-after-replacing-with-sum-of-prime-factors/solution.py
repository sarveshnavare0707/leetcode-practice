'''
You are given a positive integer n.

Continuously replace n with the sum of its prime factors.

    Note that if a prime factor divides n multiple times, it should be included in the sum as many times as it divides n.

Return the smallest value n will take on.
'''

class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            prime_sum = self.sumOfPrimeFactors(n)
            if prime_sum == n:
                return n
            
            n = prime_sum
    
    def sumOfPrimeFactors(self, n: int) -> int:
        total = 0
        
        while n % 2 == 0:
            total += 2
            n //= 2
        
        i = 3
        while i * i <= n:
            while n % i == 0:
                total += i
                n //= i
            i += 2
        
        if n > 2:
            total += n
            
        return total

if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestValue(15))  # Output: 5
    print(sol.smallestValue(12))  # Output: 5
    print(sol.smallestValue(6))   # Output: 5
    print(sol.smallestValue(4))   # Output: 4
    print(sol.smallestValue(2))   # Output: 2