def solve(stack, k):
    if k == 1:
        delted_ele =  stack[len(stack) -1]
        stack.pop()
        return delted_ele
    else:
        temp = stack.pop()
        mid = solve(stack, k-1)
        stack.append(temp)
        return mid

def delete_middle_element(stack):
    mid_index = len(stack)//2 + 1
    mid_value = solve(stack, mid_index)
    return mid_value

stack = [4,9,5,1,6,8] # bottom -> top
print("Stack before deletion: ",stack)

middle_element = delete_middle_element(stack)
print("Deleted element: ", middle_element)
print("Stack after deletion: ",stack)