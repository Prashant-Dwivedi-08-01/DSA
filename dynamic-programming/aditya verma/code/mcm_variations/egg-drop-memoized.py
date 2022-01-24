#*
#* Optimized leetcode solution: https://leetcode.com/problems/super-egg-drop/discuss/792736/CPP-Explained-Recursive-greatermemoization-greateroptimization-greaterDP-oror-Well-Explained-oror-Easy-to-unserstand
def Solve(eggs, floors, memo):
    if floors == 0 or floors == 1:
        return floors
    if eggs == 1:
        return floors
    
    key = (eggs, floors)
    if key in memo.keys():
        return memo[key]
  
    count = float('inf')
    for i in range(1, floors+1):
        temp = 1 + max(Solve(eggs, floors-i, memo), Solve(eggs-1, i-1, memo))
        count = min(count, temp)
    memo[key] = count
    return count

eggs = 2
floors = 6

attempts = Solve(eggs, floors, {})
print('# of attempts: ', attempts)