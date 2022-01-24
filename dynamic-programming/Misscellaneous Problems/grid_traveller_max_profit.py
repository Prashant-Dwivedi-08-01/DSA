''' 
For a given grid (nxm) with some cost at each cell. Calculate the maximum cost 
of going from left(starting from any position of first column) to 
right(end at any position at last column).
However, one can move in the next column in only three ways
a) right_up (r-1, c+1)
b) right    (r, c+1)
c) right_down (r+1, c+1)

INPUT:
1st line: n
2nd line: m
next n lines -> 'm1 m2 ...'
'''

#! Look at the editorial grid_traveller_max_profit Solution

def solve(grid, n, m):
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        dp[i][m-1] = grid[i][m-1]

    for c in range(m-2,-1,-1):
        for r in range(n):
            if r==0:
                dp[r][c] = grid[r][c] + max(dp[r][c+1], dp[r+1][c+1])
            elif r==(n-1):
                dp[r][c] = grid[r][c] + max(dp[r-1][c+1], dp[r][c+1])
            else:
                dp[r][c] = grid[r][c] + max(dp[r-1][c+1], dp[r][c+1],dp[r+1][c+1])
    # for row in dp:
    #     print(row)
    mx = -float('inf')
    for i in range(n):
        mx = max(mx,dp[i][0])
    return mx


n = int(input())
m = int(input())

grid = []
for i in range(n):
    row = input()
    grid.append(list(map(int, row.split(" "))))
print(solve(grid,n,m))