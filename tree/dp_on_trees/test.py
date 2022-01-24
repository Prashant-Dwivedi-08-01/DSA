l = [2,4,6,8,10,12,14,16]

def func(x):
  if x%4 == 0:
    return x
  
# filter out the numbers that are divisible by 4
ans = list(filter(fun, l))
print(ans)