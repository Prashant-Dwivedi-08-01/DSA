# Skip the specified string

def skip_string(string, result):
    if len(string) ==  0:
        return result
    if not string.startswith("apple"):
        result += string[0]
        return skip_string(string[1:], result)
    else:
        return skip_string(string[5:], result)

s = "hello-apple-is-good-apple"
ans = skip_string(s, "")
print(ans)