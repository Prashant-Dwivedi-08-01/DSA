"""
Look at the image in images folder.
At each node, we check if;
a) No. of Opening Bracket if less than the number of closing then we make both the calls
b) Otherwise we make call for only the opening bracket
c) Also, if number of opening bracket becomes zero then we don't call opening bracket call, only closing

* Underlying Logic: In any string at any moment, the number of closing must be less than or equal
* to the number of opening bracket

"""
def generate_balanced_parenthesis(pres,  o, c):
    if o == c == 0:
        res = []
        res.append(pres)
        return res

    res = []
    if o < c and o > 0:
        res.extend(generate_balanced_parenthesis(pres + ")", o, c - 1))
        res.extend(generate_balanced_parenthesis(pres + "(", o - 1, c))
    elif o == c:
        res.extend(generate_balanced_parenthesis(pres + "(", o - 1, c))
    elif o == 0:
        res.extend(generate_balanced_parenthesis(pres + ")", o, c - 1))
    return res

n = 3
ans = generate_balanced_parenthesis("",  n, n)
print(ans)