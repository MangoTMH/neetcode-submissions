from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)

        while lower <= upper:
            hours = 0
            mid = (lower + upper) // 2
            check = mid
            for i in piles:
                hours += ceil(i/check)
            if hours <= h:
                upper = mid - 1
            else:
                lower = mid + 1

        return lower