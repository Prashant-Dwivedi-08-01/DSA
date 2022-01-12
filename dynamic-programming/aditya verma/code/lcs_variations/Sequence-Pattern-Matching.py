#
#* Check if sequence S1 is present in S2
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

s1 = "AXY"
s2 = "AKJXPOY"

n = len(s1)
m = len(s1)
memo = {}
lcs_len = lcs(s1, s1, n, m, memo)
#* If lcs length is same as that of the string length to be mathced then that means
#* string to match is entirely included in LCS ans that furthur means that string 1 is
#* completly present in s2
if lcs_len == n:
    print("Yes")
else:
    print("No")