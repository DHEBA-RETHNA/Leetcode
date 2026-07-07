class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        summ = 0
        s = str(n)
        for i in s:
            if int(i) != 0:
                x = x * 10 + int(i)
                summ += int(i)
        return x * summ