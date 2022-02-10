# Here we have the binary Matrix like one below
"""
0 1 1 0
1 1 1 1 
1 1 1 1
1 1 0 0

"""
# We need the maximum area of any possible rectangle
# SOLUTION: Look at the image in images
from maximum_histogram_area import maximum_histogram_area

def maximum_area_binary_matrix(mat):
    row = mat[0]
    mx = maximum_histogram_area(row)
    for new_row in mat:
        row = list(map(lambda x,y:  x+y if x!=0 else 0, new_row, row))
        mx = max(mx, maximum_histogram_area(row))
    return mx

mat = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0]
]
print(maximum_area_binary_matrix(mat))