"""
*Question: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/submissions/
*Logic: 
Simple greedy approach, at every instance select only that triplet whose all elements are
less than the corresponding target triplets elements.

Maintain a present triplet which will eventually become the target triplet, everytime do max operation
between the selected triplet from above rationale and the present triplet and keep moving.

At any instance if we encounter that present has become target , return true, if loop is over then it
means out present can't be target, return false

"""

class Solution:
    def mergeTriplets(self, triplets, target) -> bool:
        present = [0, 0, 0]
        for t in triplets:
            temp = list(map(lambda x,y: x <= y, t, target)) # WE ONLY PROCESS THAT TRIPLET IN WHICH ALL THE VALUES ARE LESS THAN THE CORRESPONDING TARTGET VALUES
            if all(temp):
                present = list(map(lambda x, y: x if x > y else y, t, present))
            if present == target:
                return True
        return False