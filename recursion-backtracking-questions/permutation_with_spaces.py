def permutation_with_space(s, curr):
    if len(s) == 0:
        print(curr)
        return
    if len(s) != 1:
        permutation_with_space(s[1:], curr + s[0] + " ")
    permutation_with_space(s[1:], curr + s[0])

s = "ABC"
permutation_with_space(s,"")