#
#! heapq is a binary heap, with O(log n) push and O(log n) pop

from heapq import heapify, heappush, heappop

class MinHeap:
    def __init__(self) -> None:
        self.heap = []
        heapify(self.heap)
    
    def push(self, val):
        heappush(self.heap, val)

    def pop(self):
        try:
            return heappop(self.heap)
        except IndexError:
            return None
            
    def size(self):
        return len(self.heap)

    def getMin(self):
        return self.heap[0]

class MaxHeap:
    def __init__(self) -> None:
        self.heap = []
        heapify(self.heap)
    
    def push(self, val):
        heappush(self.heap, -1*val)

    def pop(self):
        try:
            return -1*heappop(self.heap)
        except IndexError:
            return None
        
    def size(self):
        return len(self.heap)

    def getMax(self):
        return -1*self.heap[0]