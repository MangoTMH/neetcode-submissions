class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        answer = []

        for i, n in enumerate(sort):
            if n > 0:
                break
            if (i > 0 and sort[i] == sort[i - 1]):
                    continue 
            l = i + 1 
            r = len(sort) - 1
            while l < r:  
                if (n + sort[l] + sort[r] > 0):
                    r -= 1
                elif (n + sort[l] + sort[r] < 0):
                    l += 1
                else:
                    answer.append([n,sort[l], sort[r]])
                    l += 1
                    r -= 1
                    while l < r and sort[l] == sort[l - 1]:
                        l += 1
                    while l < r and sort[r] == sort[r + 1]:
                        r -= 1

        return answer
