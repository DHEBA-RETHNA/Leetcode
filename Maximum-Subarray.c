int maxSubArray(int* nums, int n) {
    int max = nums[0], sum = 0;
    for(int i = 0; i < n; i++)
    {
        /*sum = nums[i];
        for(int j = i + 1; j < n; j++)
        {
            sum += nums[j];
            if (nums[j] > sum)
                sum = nums[j]; //For [-2, 1] ans: 1
            if (sum > max)
                max = sum;
        }*/
        sum = sum + nums[i];
        if(sum > max)
            max = sum;
        if(sum < 0) sum = 0;
    }
    return max;
}