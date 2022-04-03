"""
Return k largest elements from an array

Heap: Min Heap
Time: O(nlog(K))

"""
from implementation import MinHeap

def k_larget(arr, k):
    min_heap = MinHeap()

    for i in arr:
        min_heap.push(i)
        if min_heap.size() > k:
            min_heap.pop()
    
    ans = []
    while min_heap.size() != 0:
        ans.append(min_heap.pop())
    return ans

if __name__ == "__main__":
    arr = [3,9,5,1,6,8,10]
    ans = k_larget(arr, 3)
    print(ans)