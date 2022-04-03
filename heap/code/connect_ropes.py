"""
* Question
Given an array representing the length of i'th rope. We need to connect each of this rope. The cost
of connecting the ropes at any moment is equal to the sum of the lengths of both the rope.
Eg: For coonnecting the ropes of length 3 and 5, is 8.
Eg: arr = [1, 3, 5, 4, 2]
First we conncect 3 and 5, cost = 8 ( new rope of length 8)
then we connect 8 and 1, cost = 9 ( new rope of length 9)
then we connect 4 and 2, cost = 6 ( new rop of length 6)
finally we connect 9 and 6 = 15 ( final rope length 15)

total cost = 8 + 9 + 6 + 15 = 37
Final length will always be equal to sum of all the ropes.

Connect all the ropes in such a manner that cost is minumum

* Logic
Simple logic says, at any time, choose two ropes of minimum length.
Eg: [1, 2, 3, 4, 5]
Ans: 
first 1 + 2 = 3   pres_arr => [3, 3, 4, 5]
then  3 + 3 = 6   pres_arr => [6, 4, 5]
then  4 + 5 = 9   pres_arr => [9, 6]
then  9 + 6 = 15  pres_arr => []
cost = 3 + 6 + 9 +15 = 33

For this we can create a min_heap, which throws the min element always.
So, pop the two min ele, make the new rope and then push the new rope back into heap
"""
from implementation import MinHeap

def connect_ropes(ropes):
    min_heap = MinHeap()
    cost = 0
    for rope in ropes:
        min_heap.push(rope)

    while min_heap.size() > 1: # loop till we have two ropes
        r1 = min_heap.pop()
        r2 = min_heap.pop()

        cost += r1 + r2
        length = r1 + r2

        min_heap.push(length)

    return cost
if __name__ == '__main__':
    ropes = [1, 2, 3, 4, 5]
    ans = connect_ropes(ropes)
    print(ans)