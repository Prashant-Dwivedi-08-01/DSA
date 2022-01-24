import sys

def mcm(matrix_array, i, j, memo):
    if i >= j:
        return 0
    
    key = (i,j)
    if key in memo.keys():
        return memo[key]

    # loop over
    min_ans = sys.maxsize 
    for k in range(i, j):
        temp_ans = mcm(matrix_array, i, k, memo) + mcm(matrix_array, k+1,j, memo) +\
             matrix_array[i-1]*matrix_array[k]*matrix_array[j]
        min_ans =  min(min_ans, temp_ans)
        
    memo[key] = min_ans
    return memo[key]

matrix_array = [40, 20, 30, 10, 30] # 40X20, 20X30, 30X10, 10X30
i = 1
j = len(matrix_array)-1
print(mcm(matrix_array, i, j, {}))