class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = "aeiouAEIOU"
        hasVowel = False
        hasConsonant = False
        for ch in word:
            if ch.isalpha():
                if ch in vowels:
                    hasVowel = True
                else:
                    hasConsonant = True
            elif ch.isdigit():
                continue
            else:
                return False
        return hasVowel and hasConsonant