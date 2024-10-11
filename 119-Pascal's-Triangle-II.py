class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(rowIndex+1):
\t        inlist = [1]*(i+1)
\t        if i >= 2:
\t            for j in range(len(ans[i-1])-1):
\t                value = ans[i-1][j] + ans[i-1][j+1]
\t                inlist[j+1] = value
\t        ans.append(inlist)
        return ans[-1]