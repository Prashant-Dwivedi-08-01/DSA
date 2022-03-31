from heapq import heapify, heappop, heappush

min_heap = []

heapify(min_heap)

heappush(min_heap, 40)
heappush(min_heap, 30)
heappush(min_heap, 20)
heappush(min_heap, 10)

for i in range(len(min_heap)):
    print(heappop(min_heap))
