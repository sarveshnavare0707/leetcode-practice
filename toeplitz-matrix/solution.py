'''
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
'''

class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        for m1 in range(0,len(matrix)-1):
            for m2 in range(0,len(matrix[0])-1):
                if matrix[m1][m2]!=matrix[m1+1][m2+1]:
                    return False
        return True

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    s = Solution()
    print(s.isToeplitzMatrix(matrix))