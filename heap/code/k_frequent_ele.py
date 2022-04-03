"""
* Question: 
For the given array return k most frequent elements

* Logic:
We can heap in which we can store the pair(freq, ele) and this heap will be min_heap so the 
greatest elements would be at the bottom of the heap. Whenever the size of min_heap becomes
more than the K, then we simply pop the top, and remaing K are the K largest pairs in the
min_heap. [ In min_heap, the smallest are at the top, and largest at the bottom. We need 
greatest thus we have choosen the min_heap as we keep popping out from the min_heap]
"""

from heapq import heapify, heappop, heappush
from collections import defaultdict

def k_most_frequent(arr, k):
    count_arr = defaultdict(int)
    for i in arr:
        count_arr[i] += 1

    min_heap = []
    heapify(min_heap)

    for key, val in count_arr.items():
        heappush(min_heap, (val, ))
        if len(min_heap) > k:
            heappop(min_heap)

    ans = []
    while len(min_heap) > 0:
        ans.append(heappop(min_heap)[1])
    return ans

if __name__ == "__main__":
    arr = [1, 1, 1, 3, 2, 2, 4]
    ans = k_most_frequent(arr, 2)
    print(ans)