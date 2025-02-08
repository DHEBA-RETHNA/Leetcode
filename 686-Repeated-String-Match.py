class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        c = a
        for i in range(len(b) // len(a) + 2):
            if b in c:
                return len(c) // len(a)
            c += a
        return -1