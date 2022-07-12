"""
* LOGIC: 
*1. -> From Left to Right, at any moment count of '(' cant be less than ')'
*2. -> From Right to Left, at any moment count of ')' cant be less than '('

* 1 ensures that every closing bracket have there corresponding opening bracket
* 2 ensures that every opening bracket have there corresponding closing bracket


"""

def isValid(s):

    #! LEFT TO RIGHT
    left_open = 0 # count of (
    left_close = 0 # count of )
    
    for i in s:
        if i == '(':
            left_open += 1
        else:
            left_close += 1
        
        if left_close < left_open:
            return False

    #! RIGHT TO LEFT
    right_open = 0
    right_close = 0

    s = s[::-1]
    for i in s:
        if i == '(':
            right_open += 1
        else:
            right_close += 1
        
        if right_open > right_close:
            return False
    
    return True

s = "()()()("
print(isValid(s))