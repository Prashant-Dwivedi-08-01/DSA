def helper(array, n, total_sum, current_sum, desired_diff, memo):
    if(n<= 0):
        difference = current_sum - (total_sum - current_sum)
        if difference == desired_diff:
            return 1
        else:
            return 0

    key = (n-1, current_sum)
    if key in memo.keys():
        return memo[key]

    memo[key] = helper(array, n-1, total_sum, current_sum + array[n-1], desired_diff, memo) + \
                helper(array, n-1, total_sum, current_sum, desired_diff, memo)
    return memo[key]

array = [2,5,3,1]
n = len(array)
total_sum = sum(array)
current_sum = 0
desired_diff = 1
memo = {}
print(helper(array,n,total_sum, current_sum,desired_diff, memo))