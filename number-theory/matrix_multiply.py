def matrix_multiply(mat_a, mat_b):
    n_a = len(mat_a)
    m_a = len(mat_a[0])

    n_b = len(mat_b)
    m_b = len(mat_b[0])

    if m_a != n_b:
        return None

    n_res = n_a
    m_res = m_b
    res = [[0 for i in range(m_res)] for j in range(n_res)]

    for i in range(n_res):
        for j in range(m_res):
            temp = 0
            for k in range(m_a): # m_a or n_b any would do
                temp += mat_a[i][k] * mat_b[k][j]
            res[i][j] = temp
    
    return res
    
if __name__ == "__main__":
    mat_a = [
        [1,2],
        [1,2],
        [1,2]
    ]

    mat_b = [
        [4,1,5],
        [0,1,5]
    ]

    res = matrix_multiply(mat_a, mat_b)
    print(res)