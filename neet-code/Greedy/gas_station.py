"""
Simple Logic:  means that we know if we run out of fuel say at some ith gas station.
All the gas station between ith and starting point are bad starting point as well.

GOOD SOLUITON: https://leetcode.com/problems/gas-station/discuss/1706142/JavaC%2B%2BPython-An-explanation-that-ever-EXISTS-till-now!!!!
"""

class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        if sum(cost) > sum(gas):
            return -1
    
        res = 0
        total = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            
            if total < 0:
                total = 0
                res = i + 1
        return res