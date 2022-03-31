from heapq import heapify, heappop, heappush

min_heap = []

heapify(min_heap)

#* For max heap we have to invert the values while storing and re-invert them back on pop

heappush(min_heap, -1*40)
heappush(min_heap, -1*30)
heappush(min_heap, -1*20)
heappush(min_heap, -1*10)

for i in range(len(min_heap)):
    print(-1*heappop(min_heap))
