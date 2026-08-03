class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most_water = 0

        i = 0
        j = len(heights) - 1
        while i < j:
            current_water = (j - i)* min(heights[i], heights[j])
            if current_water > most_water:
                most_water = current_water
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return most_water