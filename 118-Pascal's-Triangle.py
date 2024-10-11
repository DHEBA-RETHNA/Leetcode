class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1,numRows+1):
\t        inlist = [1]*i
\t        if i > 2:
\t            for j in range(len(ans[i-2])-1):
\t                value = ans[i-2][j] + ans[i-2][j+1]
\t                inlist[j+1] = value
\t        ans.append(inlist)
        return ans