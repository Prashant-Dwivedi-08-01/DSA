# Here, we find the next smaller element to the left of the given num in array

def next_smaller_left(arr):
    stack = []
    ans = []
    for i in range(0, len(arr)):
        if len(stack) == 0:
            ans.append(-1)
        elif arr[i] > stack[len(stack)-1]:
            ans.append(stack[len(stack)-1])
        else:
            while(len(stack) > 0 and arr[i] < stack[len(stack)-1]):
                stack.pop()
            if len(stack) == 0:
                ans.append(-1)
            else:
                ans.append(stack[len(stack)-1])     
        stack.append(arr[i])
    return ans
arr = [4,5,2,10,8]
print(next_smaller_left(arr))