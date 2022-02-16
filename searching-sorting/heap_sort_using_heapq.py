from heapq import heapify, heappush, heappop

def heapsort(arr, length_of_array):
    # heapify the arr
    heapify(arr)

    sorted_arr = []
    while length_of_array > 0:
        sorted_arr.append(heappop(arr))
        length_of_array -= 1
    
    return sorted_arr


arr = [9,2,7,4,0,2,1]
arr = heapsort(arr, len(arr))
print(arr)