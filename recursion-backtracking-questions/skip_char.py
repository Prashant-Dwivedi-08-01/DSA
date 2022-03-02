# Skip the character specified and return the result array
def skip_char(string, result):
    if len(string) == 0:
        return result
    if string[0] != 'a':
        result += string[0]
    return skip_char(string[1:], result)


string = "baccadahhadac"
ans = skip_char(string, "")
print(ans)