class Solution:
    def main(self, x):
        rev = 0
        while (x > 0):
            y = x % 10
            x //= 10
            rev = rev * 10 + y
        if (rev < -2147483647 or rev > 2147483648):
            return 0
        return rev
    def reverse(self, x: int) -> int:
        if (x < 0):
            x = -x
            ans = self.main(x)
            return -ans
        else:
            ans = self.main(x)
            return ans
    