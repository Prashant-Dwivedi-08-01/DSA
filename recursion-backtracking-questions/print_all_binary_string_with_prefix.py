"""
Question: For given N, print all the possible binary strings of size N, in which
for any prefix, the number of 1's is always greater than or equal to number of 0's

Logic: Look at the Image( #*Image is for strictly greater than )
Here, we maintain the number of zeros and ones used so far. Zeros ans Ones can be maximum N.
Whenever, the number of 1's is greater than the number of 0's by 1 then only we can make calls
for both 1 and 0. Otherwise only, call for 1.

*Underlying Logic: For any moment the number of 1's cannot be greater than or numbwer of 0's

"""

def solve(pres, ones, zeros, k):
    if len(pres) == k:
        print(pres)
        return
    
    diff = zeros - ones
    if diff > 0:
        solve(pres + "0", ones, zeros-1, k)
        solve(pres + "1", ones-1, zeros, k)
    else:
        solve(pres + "1", ones-1, zeros, k)

n = 3
solve("",n, n, n)