#
#? METHOD 1
#! returning the count every time and incrementing count.
#* SIMILAR TO RETURN ARRAY LIST

def grid_traveller_m1(n,m,count):
    if n == 1 and m == 1:
        count += 1
        return count
    
    #! NOTE: count is integer which is immutable thus a new one is created. Hence, we need to updated
    #!       it by stoing the result from calls back in count var.
    #!       UNLIKE the list in subsets problem, as list are mutable and thus they get updates in each call
    if n != 1:
        count = grid_traveller_m1(n-1,m,count)
    if m != 1:
        count = grid_traveller_m1(n,m-1,count)
    return count



#? METHOD 2
#! Here we sum the results from the two calls. 
#! As part of result, we return 1 for (1,1) grid and return 0 if 
#! exploration is not possible
#* BUT HERE WE ARE MAKING EXTRA CALLS IN WHICH WE IDENTIFY THAT THIS 
#* CALL IS INVALID AND RETURN 0
def grid_traveller_m2(n,m):
    if n == 1 and m == 1:
        return 1
    
    if n == 0 or m == 0:
        return 0

    return grid_traveller_m2(n-1,m) + grid_traveller_m2(n,m-1)
  

n = 3
m = 3
ans = grid_traveller_m1(n,m,0)
print(ans)