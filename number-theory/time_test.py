import time
from matrix_exponention import matrix_exponentiation
from matrix_multiply import matrix_multiply
from print_matrix import print_matrix

mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
I = [
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ]
n = 25
ans = I.copy()

t1 = time.time()
print_matrix(matrix_exponentiation(mat, n))
# for i in range(n):
#     ans = matrix_multiply(mat, ans)
# print_matrix(ans)
t2 = time.time()
print(t2-t1)

