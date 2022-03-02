
def count_permutations(string, present_ans):
    if len(string) == 0:
        print(present_ans)
        return 1
    
    n = len(present_ans)
    char = string[0]
    count = 0
    for i in range(n + 1):
        left = present_ans[:i]
        right = present_ans[i:]
        count = count + count_permutations(string[1:], present_ans=left + char + right) 
    return count

string = "abcde"
count = count_permutations(string, "")
print(count)