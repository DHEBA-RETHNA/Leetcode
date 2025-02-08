class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s2 = s + s
        s3 = s2[1:-1]
        if s in s3:
            return True
        else:
            return False