def helper(symbols, i, j, isTrue):
    if i > j:
        return 0
    
    if i == j:
        if isTrue:
            if symbols[i] == True:
                return 1
            else:
                return  0
        else:
            if symbols[i] == False:
                return 1
            else:
                return 0
    k = i+1
    ans = 0
    while( k < j):
        left_true = helper(symbols, i, k-1, True)
        left_false = helper(symbols, i, k-1, False)
        right_true = helper(symbols, k+1, j, True)
        right_false = helper(symbols, k+1, j, False)
        
        if symbols[k] == '&':
            if isTrue == True:
                ans = ans + left_true*right_true
            else:
                ans = ans + left_false*right_true + left_true*right_false +  left_false*right_false
        elif symbols[k] == '|':
            if isTrue == True:
                ans = ans + left_true*right_false + left_false*right_true + left_true*right_true
            else:
                ans = ans + left_false*right_false
        elif symbols[k] == '^':
            if isTrue == True:
                ans = ans + left_true*right_false + left_false*right_true
            else:
                ans = ans + left_false*right_false + left_true*right_true
        
        k += 2
    return ans

symbols = "T|T&F^T"
i = 0
j = len(symbols) - 1
isTrue = True
print(helper(symbols, i, j, isTrue))