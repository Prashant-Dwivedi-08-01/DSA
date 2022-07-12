
"""
*Logic: https://youtu.be/B7m8UmZE-vw?t=380

"""
class Solution:
    def partitionLabels(self, s: str):
        last_idx_map = dict.fromkeys(s)
        s_rev = s[::-1]
        n = len(s)
        for i in last_idx_map.keys():
            last_idx_map[i] = n - 1 - s_rev.find(i)
        
        output = []
        size = 0
        end = 0

        for index, ch in enumerate(s):
            last_idx = last_idx_map[ch]

            if last_idx <= end:
                size += 1

            else: 
                end = last_idx
                size += 1

            if index == end:
                output.append(size)
                size = 0

        return output

obj = Solution()
s = "eccbbbbdec"
print(obj.partitionLabels(s))
