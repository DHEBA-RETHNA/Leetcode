class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) == len(goal):
            da = s + s
            if goal in da:
                return True
        return False
        