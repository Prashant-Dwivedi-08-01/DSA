def minimum_cost_to_travel_grid(grid):
    r = len(grid)
    c = len(grid[0])

    dp =[ [0 for i in range(c) ] for i in range(r)]

    for i in range(r):
        for j in range(c):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            elif i == 0:
                dp[i][j] = grid[i][j] + dp[i][j-1]
            elif j == 0:
                dp[i][j] = grid[i][j] + dp[i-1][j]
            else:
                dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])

    for row in dp:
        print(row)
    print(dp[r-1][c-1])


grid = [
    [3,2,1,3],
    [1,9,2,3],
    [9,1,5,4]
]

minimum_cost_to_travel_grid(grid)