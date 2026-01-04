'''
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

    position[i] is the position of the ith car (in miles)
    speed[i] is the speed of the ith car (in miles per hour)

The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.
'''

class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        arrival_time = 0
        
        for pos, spd in cars:
            current_time = (target - pos) / spd
            
            if current_time > arrival_time:
                fleets += 1
                arrival_time = current_time
            
        return fleets
    
if __name__ == "__main__":
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    
    solution = Solution()
    result = solution.carFleet(target, position, speed)
    print(result)  # Output: 3