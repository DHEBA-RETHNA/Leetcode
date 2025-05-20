class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        min = float('inf')
        for i in range(1, len(arr)):
            val = abs(arr[i] - arr[i - 1])
            if val < min:
                min = val
                ans = [[arr[i - 1], arr[i]]]
            elif val == min:
                ans.append([arr[i - 1], arr[i]])
        return ans