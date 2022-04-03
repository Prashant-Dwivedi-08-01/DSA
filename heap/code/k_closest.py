"""
* Question:
Return the k closest elements to the x in the array

* Logic:
Susbtract entire array from x and sort that difference. Sorting upto K elements only, thus O(nlog(K)).
Since we need the smallest difference so the element to be at closest, we will make use of max heap here

"""
from heapq import heappop, heapify, heappush

def k_closest(arr, k, x):
    max_heap = []
    heapify(max_heap)

    for i in arr:
        heappush(max_heap, (-1*abs(i-x), i))
        if len(max_heap) > k:
            heappop(max_heap)
    
    ans = []
    while len(max_heap) > 0:
        ans.append(heappop(max_heap)[1])
    return ans


if __name__ =="__main__":
    arr = [5, 6, 7, 8, 9, 1, 4, 2, 10]
    ans = k_closest(arr, 2, 9)
    print(ans)