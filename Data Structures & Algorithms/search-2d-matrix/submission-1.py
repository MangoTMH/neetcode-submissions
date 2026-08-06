class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        firstO, lastO = 0, len(matrix) -1
        firstI, lastI = 0, len(matrix[0]) -1
        while firstO <= lastO:
            midO = (firstO + lastO) // 2
            if target < matrix[midO][0]:
                lastO = midO -1
            elif target > matrix[midO][-1]:
                firstO = midO + 1
            else:
                
                while firstI <= lastI:
                    midI = (firstI + lastI) // 2
                    if target < matrix[midO][midI]:
                        lastI = midI -1
                    elif target > matrix[midO][midI]:
                        firstI = midI + 1
                    else:
                        return True
                return False
        return False