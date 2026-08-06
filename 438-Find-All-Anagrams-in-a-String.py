class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        count1 = [0] * 26
        count2 = [0] * 26
        if len(s) < len(p):
            return []
        else:
            for i in p:
                count1[ord(i) - ord("a")] += 1
            for i in range(len(p)):
                count2[ord(s[i]) - ord("a")] += 1
            if count1 == count2:
                ans.append(0)
            for j in range(len(p), len(s)):
                count2[ord(s[j]) - ord("a")] += 1
                count2[ord(s[j - len(p)]) - ord("a")] -= 1
                if count1 == count2:
                    ans.append(j-len(p)+1)
        return ans