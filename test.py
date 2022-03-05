def max_to_left(arr):
    ans = []
    ans.append(arr[0])
    for num in arr[1:]:
        ans.append(max(ans[len(ans)-1], num))
    return ans 
arr = [5,4,10,1,91,5]
print(max_to_left(arr))