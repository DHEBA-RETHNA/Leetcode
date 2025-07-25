bool searchMatrix(int** matrix, int row, int* col, int t) {
    int m = row;
    int n = *col;
    int left = 0, right = m * n -1;
    while (left <= right)
    {
        int mid = (left + right) / 2;
        if (matrix[mid / n][mid % n] == t)
            return true;
        else if (matrix[mid / n][mid % n] < t)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return false;
}