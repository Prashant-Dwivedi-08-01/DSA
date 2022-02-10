# Here we need to find same i.e. next largest element but to the left of the given element

def next_greater_left(arr):
	stack = []
	ans = []
	for i in range(0, len(arr)):
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

	return ans


arr = [1,3,2,4]
print(next_greater_left(arr))