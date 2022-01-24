import sys

#
#* Look image named pallindrome-partition-logic in images folder of aditya verma
def pallindrome_partition(s, i, j, memo):
    if i>= j:
        memo[(i,j)] = 0
        return 0

    key = (i,j)
    if key in memo.keys():
        return memo[key]

    if ispallindrome(s[i:j+1]):
        memo[(i,j)] = 0
        return 0

    min_value = sys.maxsize
    for k in range(i, j):#! ideally i need to loop from k=i to k=j-1
        if ispallindrome(s[i:k+1]):
            temp_ans = 1 + pallindrome_partition(s, k+1, j, {})
        min_value =  min(min_value, temp_ans)
    memo[key] = min_value
    return memo[key]

def ispallindrome(s):
    return s == s[::-1]

s = "apjesxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
i = 0
j = len(s)-1
print(pallindrome_partition(s,i,j, {}))
# print(ispallindrome('abcba', 0, 3))

