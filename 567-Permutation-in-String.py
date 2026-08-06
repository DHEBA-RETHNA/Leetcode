from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        count1 = Counter(s1)
        for i in range(len(s2) - k + 1):
            window = s2[i:i+k]
            if Counter(window) == count1:
                return True
        return False