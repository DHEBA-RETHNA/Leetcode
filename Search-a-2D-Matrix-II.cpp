class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int t) {
        int m = matrix.size();
        int n = matrix[0].size();
        int row = m - 1, col = 0;
        while (row >= 0 && col <= n-1)
        {
            if (matrix[row][col] == t)
                return true;
            else if (matrix[row][col] < t) col++;
            else row--;
        }
        return false;
    }
};