class Solution:
    def isPalindrome(self, s: str) -> bool:
        min = 0
        max = len(s) - 1
        while min < max:
            while (min < max and not s[min].isalnum()):
                min += 1
  
            while (min < max and not s[max].isalnum()):
                max -= 1

            if s[min].lower() != s[max].lower():
                return False
            max -= 1
            min += 1
            
        return True
        