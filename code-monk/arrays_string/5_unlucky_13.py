x = 1000000009
memo = {}
# memo2 = {}

"""
! ONE VERY IMPORTANT CONCEPT WE CAME TO KNOW IS ABOUT SPLITTING THE MEMO INTO TWO WHENE THERE IS MEMORY LIMIT EXCEEDED
! TRY SPLITTING AT MIDDLE OF N, IF STILL GETTING ERROR THEN KEEP REDUCING THE ZEROS.

? LOGIC: LOOK AT THE VIDEO: https://www.youtube.com/watch?v=HFGZ1-y-1No&list=PL1YS4hYJip07A-YteNUR8qTeA_wHQarDX&index=47

"""

def solve(n):
    if n < 50000000:
        if n == 0:
            return 1 # empty string
        if n == 1:
            return 10 # string of size 1
        
        if n in memo.keys():
            return memo[n]

        temp = solve(n//2)
        temp_minus_one = solve(n//2 - 1)

        if n&1:
            temp2 = solve(n//2 + 1) # right side part
            ans = (temp*temp2 - temp*temp_minus_one) % x
        else: 
            ans = (temp*temp - temp_minus_one*temp_minus_one) % x
        
        memo[n] = ans
        return ans
    else:
        if n == 0:
            return 1 # empty string
        if n == 1:
            return 10 # string of size 1
        
        if n in memo2.keys():
            return memo2[n]

        temp = solve(n//2)
        temp_minus_one = solve(n//2 - 1)

        if n&1:
            temp2 = solve(n//2 + 1) # right side part
            ans = (temp*temp2 - temp*temp_minus_one) % x
        else: 
            ans = (temp*temp - temp_minus_one*temp_minus_one) % x
        
        memo2[n] = ans
        return ans

t = int(input())
for i in range(t):
    n = int(input())
    memo2 = {}
    ans  = solve(n)
    print(ans)
    print()