int maxProfit(int* prices, int n) {
    int profit = 0, cprofit = 0, minbuyprice = prices[0];
    for (int i = 1; i < n; i++)
    {
        if (prices[i] < minbuyprice)
            minbuyprice = prices[i];
        else
        {
            cprofit = prices[i] - minbuyprice;
            if (cprofit > profit)
                profit = cprofit;
        }
    }
    return profit;
}