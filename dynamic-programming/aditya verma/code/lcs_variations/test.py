x = 1
def a(n):
    if(n == 0):
        return 
    global x
    x = x + 1
    a(n-1)

a(5)
print(x)