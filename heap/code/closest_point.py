"""
* Question:
You are given the 2D array, represting the coordinates in plain.
Return the coordinate closes from the origin

* Logic:
Largely, we need to sort the distance between origin and each point and
then get the minimum one as the ans.

Implementation can be done easily if we use a min_heap and make the elements
of the heap as (dist_from_origin, (x, y)) and store in min heap and then return
the top
"""
from implementation import MinHeap

def closest_from_origin(coordinates):
    min_heap = MinHeap()
    for i in coordinates:
        x, y = i
        dist_from_origin_sqr = y**2 + x**2
        min_heap.push((dist_from_origin_sqr, (x,y)))
    return min_heap.getMin()

if __name__ == '__main__':
    coordinates = [
        [1, 3],
        [2, 2],
        [5, 8]
    ]
    ans = closest_from_origin(coordinates)
    print(ans)