
"""
todo:  LOGIC ==> Here we are following the divide and concor approach to get the TC of O(Log(N)).
*                If the power is even, then we keep dividing the power by 2 till we reach 0
*                If the power is negative then we split the power by seperating one power and do the same.
*          Eg:--> 2^16 = 2^8 * 2^8 then,
*                 2^8  = 2^4 * 2^4 then,
*                 2^4  = 2^2 * 2^2 then,
*                 2^2  = 2^1 * 2^1 then,
*                 2^1  = 2 *( 2^0 * 2^0) thus retunr 1.
*          For Odd 
*          Eg:--> 3^9 = 3 * (3^4 * 3^4) then,
*                 3^4  = 3^2 * 3^2 then,
*                 3^2  = 3^1 * 3^1 then,
*                 3^1  = 3 * (3^0 * 3^0) thus retunr 1.
*
! Time : O(log(n))
"""

def bin_expo(a, b):
    if b == 0:
        return 1
    ans = bin_expo(a, b//2)

    if b&1:
        return a * ans * ans
    else:
        return ans * ans

a = 2
b = 16
print(bin_expo(a, b))
