int maxArea(int* h, int n) {
    int left = 0, right = n-1, ans = 0;
    while (left < right)
    {
        int w = right - left;
        ans = fmax(ans, w * fmin(h[left], h[right]));
        if (h[left] < h[right])
            left++;
        else if (h[left] == h[right]) left++, right--;
        else
            right--;
    }
    return ans;
}