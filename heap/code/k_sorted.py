"""
* Question: 
Given an array, at each index of array the correct number is always in the range of K 
elements next to it.
Eg: arr = [6,3,1] k = 2
So here, at position 0, the number should be 1 and it is in range of 2 elements from index 0.

Sort this array completely

* Logic: 
Normally we would sort the array as it is in O(n*log(n)). But we can do better with the given
information.
Since the right element at any index is in the range of K elements, then if we sort just the K elements
each time then the time would become O(n* log(k))

"""
from implementation import MinHeap
def k_sorted(arr, k):
    ans = []
    min_heap = MinHeap()

    for i in arr:
        min_heap.push(i)
        if min_heap.size() > k:
            ans.append(min_heap.pop())
    
    while min_heap.size() > 0:
        ans.append(min_heap.pop())
    
    return ans

if __name__ == "__main__":
    arr = [6,5,3,2,8,10,9]
    ans = k_sorted(arr, 3)
    print(ans)