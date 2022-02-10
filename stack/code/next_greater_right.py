# Look at the image in images folder 
def next_greater_right(arr):
	stack = []
	ans = []
	for i in range(len(arr)-1, -1, -1):
		if len(stack) == 0:
			ans.append(-1)

		elif arr[i] < stack[len(stack)-1]:
			ans.append(stack[len(stack)-1])
		else:
			while(len(stack) > 0 and arr[i] > stack[len(stack)-1]):
				stack.pop()
			if len(stack) == 0:
				ans.append(-1)
			else:
				ans.append(stack[len(stack)-1])

		stack.append(arr[i]) 
	ans.reverse()
	return ans


arr = [1,3,2,4]
print(next_greater_right(arr))