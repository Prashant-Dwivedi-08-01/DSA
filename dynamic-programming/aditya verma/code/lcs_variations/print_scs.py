def print_scs(s1, s2):
    t = [[-1 for i in range(0,len(s2)+1)] for j in range(0,len(s1)+1)]

    # initialize
    for i in range(0, len(s1)+1):
        for j in range(0, len(s2)+1):
            if(i == 0 or j == 0):
                t[i][j] = 0
            
    for i in range(1,len(s1)+1):
        for j in range(1, len(s2)+1):
            if(s1[i-1] == s2[j-1]):
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    

    scs_string = ""
    i = len(s1)
    j = len(s2)
    while i>0:
        while j> 0:
            if s1[i-1] == s2[j-1]:
                scs_string+=s1[i-1]
                i -= 1
                j -= 1
            elif t[i-1][j] > t[i][j-1]:
                scs_string += s1[i-1]
                i -=1
            else:
                scs_string += s2[j-1]
                j-=1
    return scs_string[::-1]

s1 = "abcdaf"
s2 = "acbcf"

print(print_scs(s1, s2))
    