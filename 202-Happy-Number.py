class Solution:
    def isHappy(self, n: int) -> bool:
        \\\n = str(n)
        copy = n
        if len(n) == 1 and n[0] != '1':
            return False
        while(len(n) > 1):
            n = str(sum(pow(int(i),2) for i in n))
            if n == copy:
                return False
        return True\\\ #we need to loop even len(n) -- 1. eg: 7
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum(pow(int(i),2) for i in str(n))
        return True