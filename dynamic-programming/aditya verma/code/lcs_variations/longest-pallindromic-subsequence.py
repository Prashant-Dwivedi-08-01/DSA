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

s1 = "aacabdkacaa"

lcs_len = lcs(s1, s1[::-1], len(s1), len(s1), {})
print(lcs_len)
