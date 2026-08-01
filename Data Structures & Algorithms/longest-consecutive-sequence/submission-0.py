class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        sort = sorted(nums)
        unique = set(nums)
        check = set()

        for i in unique:
            if (i - 1) not in unique:
                check.add(i)

        answer = 0
        for j in check:
            longest = 1
            current = j

            while current + 1 in unique:
                current += 1
                longest += 1
            if longest > answer:
                answer = longest
        return answer