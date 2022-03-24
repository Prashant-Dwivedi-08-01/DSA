def re_insert(stack, item):
    if len(stack) == 0:
        stack.append(item)
        return
    temp = stack.pop()
    re_insert(stack, item)
    stack.append(temp)
    
def reverse_stack(stack, k):
    if k == 0:
        return
    temp = stack.pop()
    reverse_stack(stack, k-1)
    re_insert(stack, temp)


stack = [5,4,3,2,1]
reverse_stack(stack, len(stack))
print(stack)