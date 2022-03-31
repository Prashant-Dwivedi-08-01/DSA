"""
Return K'th samllest element of array. This can be easily done in nlog(n).

We can sort using that costs nlog(n) and then return arr[k]

But we need to implement it in nlog(k)

Using heap: Here we loop arr of n, thus O(n) and 
then for each we push in heap which is O(log(K)), k = present size of heap

Logic: Here, we keep pushing array elements in heap. Whenever the size of heap 
becomes greater than K, then we pop the top element. Proceeding in this manner we 
are left with only k elements in heap
Since it is max heap, we are having k'th smallest element at top
"""
from implementation import MaxHeap

def k_th_smallest(arr, k):
    max_heap = MaxHeap()
    for ele in arr:
        max_heap.push(ele)
        if max_heap.size() > k:
            max_heap.pop()
    return max_heap.getMax()

arr = [8,2,9,5,1,3]
k = 4
ans = k_th_smallest(arr, k)
print(ans)