class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False
        ds, dt = {}, {}
        for i in s:
            if i not in ds:
                ds[i] = s.count(i)
        for j in t:
            if j not in dt:
                dt[j] = t.count(j)
        for k in ds:
            if ds[k] != dt.get(k, 0):
                return False
        return True