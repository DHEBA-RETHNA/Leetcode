class Solution:
    def isPalindrome(self, x: int) -> bool:
        copy = x
        ans = 0
        while (x > 0):
            y = x % 10
            ans = ans * 10 + y
            x //= 10
        if (copy == ans):
            return True
        else:
            return False