int search(int* nums, int n, int t) {
    int left = 0, right = n-1;
    while(left <= right)
    {
        int mid = (left + right) / 2;
        if (nums[mid] == t)
            return mid;
        else if (t < nums[mid])
            right = mid - 1;
        else
            left = mid + 1;
    }
    return -1;
}