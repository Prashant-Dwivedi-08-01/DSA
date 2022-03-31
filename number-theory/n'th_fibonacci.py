from matrix_exponention import matrix_exponentiation
from matrix_multiply import matrix_multiply

def N_th_fibo(n):
    F_0 = 0
    F_1 = 1

    x = n - 1
    helper_matrix = [
        [1, 1],
        [1, 0]
    ]
    constant_matrix = [
        [F_1],
        [F_0]
    ]
    temp = matrix_exponentiation(helper_matrix, x)

    ans = matrix_multiply(temp, constant_matrix)

    return ans[0][0]


if __name__ == "__main__":
    n = 110
    ans = N_th_fibo(n)
    print(f"{n}th Fibo --> {ans}")