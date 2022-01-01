#
#* Here, we have the liberty to include an item more than once

def unbounded_knapsack(weight, profits, capacity, n, memo):
    if capacity == 0 or n == 0:
        return 0 #* maximum profit is 0 here

    key = (n-1, capacity)
    if key in memo.keys():
        return memo[key]

    if weight[n-1] <= capacity:
        memo[key] =  max( profits[n-1] + unbounded_knapsack(weight, profits, capacity-weight[n-1],n, memo), unbounded_knapsack(weight, profits, capacity, n-1, memo))
        return memo[key]
    else:
        memo[key]= unbounded_knapsack(weight, profits, capacity,n-1, memo)
        return memo[key]

profits =  [10,23,43,56,34]
weight =    [2,4,6,7,8] 
capacity = 15
no_of_items=  len(weight)
memo = {}

print(unbounded_knapsack(weight, profits, capacity, no_of_items, memo))