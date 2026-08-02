class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        for i in range(len(numbers)):
            sum = numbers[l] + numbers[r]
            if sum < target:
                l += 1
            if sum > target:
                r -= 1
            if sum == target:
                return [l+1,r+1]