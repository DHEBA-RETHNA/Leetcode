int canCompleteCircuit(int* gas, int n, int* cost, int m) {
    /*int totalcost = 0, totalgaas = 0;
    for (int i = 0; i < n; i++)
    {
        totalcost += cost[i];
        totalgas += gas[i];
    }
    if (totalcost > totalgas) return -1;
    int ans = 0, currgain = 0;
    for (int i = 0; i < n; i++)
    {
        currgain = currgain + gas[i] - cost[i];
        if (currgain < 0)
        {
            ans = i + 1;
            currgain = 0;
        }
    }
    return ans;*/

    int totalgain = 0, currgain = 0, ans = 0;
    for (int i = 0; i < n; i++)
    {
        currgain = currgain + gas[i] - cost[i];
        totalgain = totalgain + gas[i] - cost[i]; /*for calculating the 1st for loop, we can just calculate the totalgain*/
        if (currgain < 0)
        {
            ans = i + 1;
            currgain = 0;
        }
    }
    return totalgain < 0? -1 : ans;/*if totalgain -ve means no solution*/
}