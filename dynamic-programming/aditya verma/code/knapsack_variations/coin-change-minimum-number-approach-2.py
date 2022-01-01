
#* In DP the dimension of memoization is equal to the number of changing parameters


import sys
def helper(coins, n, target_sum, present_no_coins, memo):
    if target_sum == 0:
        return present_no_coins
    if n <= 0:
        return sys.maxsize - 1 

    #memo
    key = (n-1, target_sum, present_no_coins)
    if key in memo.keys():
        return memo[key]
    
    if target_sum >= coins[n-1]:
        include_coin = present_no_coins + 1
        exclude_coin = present_no_coins
        memo[key] = min( helper(coins, n, target_sum-coins[n-1], include_coin, memo), helper(coins, n-1, target_sum, exclude_coin, memo))
        return memo[key]
    else:
        exclude_coin = present_no_coins
        memo[key] = helper(coins, n-1, target_sum, exclude_coin, memo)
        return memo[key]


coins = [2,5,10,1]
target_sum = 27
n = len(coins)
memo = {}
result = helper(coins, n, target_sum, 0,memo)

if result == (sys.maxsize-1):
    print("-1")
else:
    print(result)
