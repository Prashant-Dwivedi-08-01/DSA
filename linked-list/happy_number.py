# Happy Number implementation using the slow fast pointer method
# https://leetcode.com/problems/happy-number/

def happy_number(n):
    slow = n
    fast = n
    while 1:
        slow = sqr(slow)
        fast = sqr(sqr(fast))
        if slow == fast:
            break

    if slow == 1:
        return True
    return False

def sqr(n):
    ans = 0
    while n > 0:
        ans += (n%10)**2
        n = n//10
    return ans

n1 = 19
n2 = 2
n3 = 65
print(str(n1) + "==>" + str(happy_number(n1)))
print(str(n2) + "==>" + str(happy_number(n2)))
print(str(n3) + "==>" + str(happy_number(n3)))
