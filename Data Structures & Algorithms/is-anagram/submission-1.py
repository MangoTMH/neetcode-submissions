class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        arr1 = []
        arr1 = list(s)
        arr1sorted = sorted(arr1)

        arr2 = []
        arr2 = list(t)
        arr2sorted = sorted(arr2)

        for i in range(len(s)):
            if arr1sorted[i] != arr2sorted[i]:
                return False
        return True