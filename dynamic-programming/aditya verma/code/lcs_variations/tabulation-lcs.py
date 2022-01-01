#
#* Look at the Imgae in adityaverma/images/lcs_tabulation.jpg

def lcs_tabulation(s1, s2):
    # make matrix of desired size
    t = [ [None]* (len(s2)+1) ]*(len(s1)+1)

    # initialization
    #* initialization in tabluation approach is just the base condition of recursize approach. Here, the base condition
    #* was when either of the string length is 0, then lcs for that case is of length 0.
    for i in range(0,len(s1) + 1):
        t[i][0] = 0
    for j in range(0,len(s2) + 1):
        t[0][j] = 0

    #* loop over the matrix from (1,1) and fill the matrix using previous entries
    for i in range(1,len(s1) + 1):
        for j in range(1,len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i][j-1], t[i-1][j])


    return t[len(s1)][len(s2)]
s1 = "xbdaks"
s2 = "aks"

print(lcs_tabulation(s1, s2))