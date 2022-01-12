#
#* Minimum deletion means the Pallindrome must be longest. This brings us to our question
#* of longest pallindrome subsequence. Ans: (String - Longest Pallindrome Subsequence). 
#* Remaining characters must be removed to make the string pallindrome so that becomes our ans
def lcs(s1, s2, n, m, memo):
    #base condition
    if n == 0 or m == 0:
        return 0
    
    #memo
    key = (n-1, m-1)
    if key in memo.keys():
        return memo[key]

    #choice diagram
    if s1[n-1] == s2[m-1]:
        memo[key] = 1 + lcs(s1, s2, n-1, m-1, memo) # since in this both chars are same that means we are including this char. Thus length of lcs increases by 1. And now whatever the remaining string gives that will be added to this 1
        return memo[key]
    else:
        memo[key] = max(lcs(s1, s2, n-1, m, memo), lcs(s1, s2, n, m-1, memo))
        return memo[key]

s1 = 'agbcba'

pallindrome_len = lcs(s1, s1[::-1], len(s1), len(s1), {})
print(len(s1)-pallindrome_len)