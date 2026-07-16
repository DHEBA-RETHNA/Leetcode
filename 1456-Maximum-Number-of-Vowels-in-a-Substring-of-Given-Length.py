class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window = s[:k]
        vowel = "aeiouAEIOU"
        ans = 0
        for i in window:
            if i in vowel:
                ans += 1
        maxx = ans
        for i in range(k, len(s)):
            if s[i] in vowel:
                ans += 1
            if s[i - k] in vowel:
                ans -= 1
            maxx = max(ans, maxx)
        return maxx