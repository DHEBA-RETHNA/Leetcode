/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* nextGreaterElement(int* nums1, int n1, int* nums2, int n2, int* rs) {
    int* res = malloc(sizeof(int) * n1);
    *rs = n1;
    for(int i = 0; i < n1; i++)
    {
        bool found = false;
        res[i] = - 1;
        for(int j = 0; j < n2; j++)
        {
            if (nums1[i] == nums2[j]) found = true;
            if (found && nums2[j] > nums1[i])
            {
                res[i] = nums2[j];
                break;
            }
        }
    }
    return res;
}