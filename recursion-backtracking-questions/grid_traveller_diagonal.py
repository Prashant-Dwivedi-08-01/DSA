def grid_traveller_diagonal(n,m):
    if n == 1 and m == 1:
        return 1
    
    if n == 0 or m == 0:
        return 0
    return grid_traveller_diagonal(n-1, m) \
            + grid_traveller_diagonal(n, m-1) \
            + grid_traveller_diagonal(n-1, m-1)
n = 4
m = 2

print(grid_traveller_diagonal(n,m))