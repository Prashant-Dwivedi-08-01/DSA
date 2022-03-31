from matrix_multiply import matrix_multiply
from print_matrix import print_matrix

def matrix_exponentiation(mat, n):
    if n == 1:
        return mat
    temp_res = matrix_exponentiation(mat, n//2)

    if n&1:
        return matrix_multiply(mat, matrix_multiply(temp_res, temp_res))
    else:
        return matrix_multiply(temp_res, temp_res)

if __name__ == "__main__":
    mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    n = 4
    ans = matrix_exponentiation(mat, n )
    print_matrix(ans)