#
#! Print Permuations
def print_permutations(string, present_ans):
    if len(string) == 0:
        print(present_ans)
        return
    
    n = len(present_ans)
    char = string[0]
    for i in range(n + 1):
        left = present_ans[:i]
        right = present_ans[i:]
        print_permutations(string[1:], present_ans=left + char + right) 


string = "aab"
print_permutations(string, "")

#! Return Permutations
def return_permutations(string, present_ans, result):
    if len(string) == 0:
        result.append(present_ans)
        return result
    
    n = len(present_ans)
    char = string[0]
    for i in range(n + 1):
        left = present_ans[:i]
        right = present_ans[i:]

        present_ans=left + char + right
        result = return_permutations(string[1:],present_ans, result) 
    return result

# string = "abc"
# ans = return_permutations(string, "", [])
# print(ans)

