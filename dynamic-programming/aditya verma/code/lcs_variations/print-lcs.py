#
#* Look at the Imgae in adityaverma/images/lcs_tabulation.jpg

def print_lcs(s1, s2):
    # make matrix of desired size
    t = [[-1 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

    # initialization
    #* initialization in tabluation approach is just the base condition of recursize approach. Here, the base condition
    #* was when either of the string length is 0, then lcs for that case is of length 0.
    for i in range(0,len(s1) + 1):
        for j in range(0,len(s2) + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
    

    #* loop over the matrix from (1,1) and fill the matrix using previous entries
    for i in range(1,len(s1) + 1):
        for j in range(1,len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i][j-1], t[i-1][j])

    for r in t:
        print(r)
    lcs_string = ""
    i = len(s1)
    j = len(s2)
    print(i)
    print(j)
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs_string += s1[i-1]
            i-=1
            j-=1
        elif t[i-1][j] > t[i][j-1]:
            i-=1
        else:
            j-=1
    

    return lcs_string[::-1]

s1 = "delete"
s2 = "leet"

print(print_lcs(s1, s2))