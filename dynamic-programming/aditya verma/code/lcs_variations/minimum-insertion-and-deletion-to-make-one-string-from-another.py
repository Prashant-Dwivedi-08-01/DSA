#
#* what minimumnumber of insertion and deletion shall be done to make the new string from given string
def lcs(s1, s2, n, m, memo):
    if n == 0 or m == 0:
        return 0
    
    key = (n-1, m-1)
    if key in memo.keys():
        return memo[key]

    if s1[n-1] == s2[m-1]:
        memo[key] = 1 + lcs(s1, s2, n-1, m-1, memo)
        return memo[key]
    else:
        memo[key] = max(lcs(s1, s2, n-1, m, memo), lcs(s1, s2, n, m-1, memo))
        return memo[key]

s1 = 'heap'
s2 = "pea"

lcs_len = lcs(s1, s2, len(s1), len(s2), {})

#minimum insertion-deletion ans
# deletion: s1 - lcs
# insertion: s2 - lcs
print("Deletion: ", len(s1)-lcs_len)
print("Insertion: ", len(s2)-lcs_len)