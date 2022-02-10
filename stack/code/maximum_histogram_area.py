# Given Histogram, find the maximum possible area.
# LOOK AT THE IMAGE IN images 
#! LOGIC: The main logic here is that, when we are on any building/histogram, let's say
#! histogram/building of size 2, then we need to find the maximum area possible from the 
#! height of present building viz. 2 here. Then we keep exploring to left and right to find 
#! all the buildings with height greater than or equal to present height viz. 2. So in other 
#! terms we are trying to find the first smaller building than ours, as then we cannot extend 
#! the present building. Proceeding in this manner we try to find the first smaller building 
#! in left and right of the present one and the we get the width and length is present buildings 
#! height, thus, we get the area here when we consider present building.

def next_smaller_right(arr):
    stack = []
    ans = []
    for i in range(len(arr)-1, -1, -1):
        if len(stack) == 0:
            ans.append(len(arr))
        elif arr[i] > arr[stack[len(stack)-1]]:
            ans.append(stack[len(stack)-1])
        else:
            while len(stack)>0 and arr[i] <= arr[stack[len(stack)-1]]:
                stack.pop()
            if len(stack) == 0:
                ans.append(len(arr))
            else:
                ans.append(stack[len(stack)-1])
        stack.append(i)
    ans.reverse()
    return ans

def next_smaller_left(arr):
    stack = []
    ans = []
    for i in range(len(arr)):
        if len(stack) == 0:
            ans.append(-1)
        elif arr[i] > arr[stack[len(stack)-1]]:
            ans.append(stack[len(stack)-1])
        else:
            while len(stack)>0 and arr[i] <= arr[stack[len(stack)-1]]:
                stack.pop()
            if len(stack) == 0:
                ans.append(-1)
            else:
                ans.append(stack[len(stack)-1])
        stack.append(i)
    return ans

def maximum_histogram_area(histogram):
    next_smaller_right_index = next_smaller_right(histogram)
    next_smaller_left_index = next_smaller_left(histogram)
    
    width_array = list(map(lambda x,y:x-y-1, next_smaller_right_index, next_smaller_left_index))
    area = list(map(lambda x,y: x*y, width_array, histogram))
    
    # print("NSR: ",next_smaller_right_index)
    # print("NSL: ",next_smaller_left_index)
    # print("WIDTH: ",width_array)
    # print("AREA: ",area)

    return max(area)
                            

if __name__ == "__main__":
    histogram = [1]
    print("Maximum Area: ", maximum_histogram_area(histogram))
