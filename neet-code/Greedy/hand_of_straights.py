# https://leetcode.com/problems/hand-of-straights/
# LOGIC: Look at the image in images
"""
We are using elements from min heap so that we can have next smallest element
as things should be consecutive.

We pop the elements from the min heap whose count goes to zero.

If we pop 1 from min heap and groupSize is 3 then we find 1,2,3 in count dict and 
reduce there count by 1. If any element( 1,2,3) is not present then we return false
"""

from collections import defaultdict
from heapq import heapify, heappop
class Solution:
    def isNStraightHand(self, hand, groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = defaultdict(int)
        for i in hand:
            count[i] += 1
        
        min_heap = list(count.keys())
        heapify(min_heap)

        while len(min_heap):
            min_val = min_heap[0]

            for i in range(groupSize):
                if count[min_val]:
                    count[min_val] -= 1

                    if count[min_val] == 0:
                        heappop(min_heap)
                    min_val = min_val + 1
                else:
                    return False
        return True

obj = Solution()
hand = [8,10,12]

groupSize = 3

ans = obj.isNStraightHand(hand, groupSize)
print(ans)