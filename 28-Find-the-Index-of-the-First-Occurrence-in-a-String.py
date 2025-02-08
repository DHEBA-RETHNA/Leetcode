class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while (i < (len(haystack) - len(needle) + 1)):
            j = 0
            while (j < len(needle)):
                if haystack[i+j] == needle[j]:
                    j += 1
                else:
                    break
            if j == len(needle):
                return i
            i += 1
        return -1