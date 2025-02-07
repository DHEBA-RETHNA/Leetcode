class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = \\
        word = min(strs, key = len)
        for j in range(len(word)):
            for i in range(len(strs) - 1):
                if strs[i][j] != strs[i + 1][j]:
                    return ans
            ans += strs[0][j]
        return ans
