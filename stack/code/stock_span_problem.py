# Here we need to calculate the number of consecutive smaller than or equal stock prices
# of previous days, for any given day. 
# Eg: [100,80,60,70,60,75,85] then for 75 it would be (60, 70, 60, 75) i.e 4 days

# SOLUTION: Here, we need to go back till we find the first greater element because then 
# actually we will be doing the same thing, i.e. covering the consecutive smaller numbers 
# than present

# Here, we are storing index of days array as ans to the problem of storing the first greater
# and then we simply substracting the index with ans array's index
# LOOK at the image in images for clear understanding

def stock_span_problem(days):
    stack = [] # here we are storing the index of the numbers and not the actual values
    ans = []  # here in ans we are storing the index and not the actual values
    for i in range(len(days)):
        if len(stack) == 0:
            ans.append(-1)
        elif days[i] < days[stack[len(stack)-1]]:
            ans.append(stack[len(stack)-1])
        else:
            while len(stack) > 0 and days[i] > days[stack[len(stack)-1]]:
                stack.pop()
            if len(stack) == 0:
                ans.append(-1)
            else:
                ans.append(stack[len(stack)-1])
        stack.append(i)
    print(ans)
    ans = [i - num for i, num in enumerate(ans)]
    return ans

days = [100,80,110,70,60,75,85]
print(stock_span_problem(days))