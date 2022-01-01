#
#* Look at the Image in adityaverma/images to check the logic of lcs

def lcs(s1, s2, n, m, memo, length):
    #base condition
    if n == 0 or m == 0:
        return length
    
    #memo
    key = (n-1, m-1, length)
    if key in memo.keys():
        return memo[key]

    #choice diagram
    if s1[n-1] == s2[m-1]:
        memo[key] = length = lcs(s1, s2, n-1, m-1, memo, length+1) 
    memo[key] = length = max(length, max(lcs(s1, s2, n-1, m, memo, 0), lcs(s1, s2, n, m-1, memo, 0)))

    return length
s1 = "abcdeg"
s2 = "xbxdev"

nums1 = [0,0,0,0,0]
nums2 = [0,0,0,0,0]

n = len(nums1)
m = len(nums2)
memo = {}
print(lcs(nums1, nums2, n, m, memo,0))