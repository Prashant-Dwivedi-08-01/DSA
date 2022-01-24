import sys

#
#* Look image named pallindrome-partition-logic in images folder of aditya verma
def pallindrome_partition(s, i, j, memo):
    if i>= j or ispallindrome(s, i, j):
        return 0


    key = (i,j)
    if key in memo.keys():
        return memo[key]

    min_value = sys.maxsize
    for k in range(i, j):#! ideally i need to loop from k=i to k=j-1
        temp_ans = 1 + pallindrome_partition(s, i, k, memo) + \
            pallindrome_partition(s, k+1, j, memo)

        min_value =  min(min_value, temp_ans)
    memo[key] = min_value
    return memo[key]

def ispallindrome(input, start, end):

    # Using two pointer technique to check pallindrome
    while (start < end):
        if (input[start] != input[end]):
            return False;
        start += 1
        end -= 1
    return True;

s = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
i = 0
j = len(s)-1
print(pallindrome_partition(s,i,j, {}))
# print(ispallindrome('abcba', 0, 3))

