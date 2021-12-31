import sys
def helper(coins, n, target_sum, memo):
    if target_sum == 0:
        return 0
    if n <= 0:
        return sys.maxsize -1 # as we are doing + 1 on return

    #memo
    key = (n-1, target_sum)
    if key in memo.keys():
        return memo[key]
    
    if target_sum >= coins[n-1]:
        memo[key] = min(1 + helper(coins, n, target_sum-coins[n-1], memo), helper(coins, n-1, target_sum, memo))
        return memo[key]
    else:
        memo[key] = helper(coins, n-1, target_sum, memo)
        return memo[key]

coins = [2,5,10,1]
target_sum = 27
n = len(coins)
result = helper(coins, n, target_sum,{})
print(result)
if result == sys.maxsize:
    print("-1")
else:
    print(result)