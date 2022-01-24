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
    l = 1
    h = floors
    while(l <= h):
        mid = (l+h)//2
        worst_left_attempts = Solve(eggs-1, mid-1, memo)
        worst_right_attempts = Solve(eggs, floors-mid, memo)
        temp = 1 + max(worst_left_attempts , worst_right_attempts) # we need max of all the possible attempts to give the minimum number of attempts
        if worst_left_attempts < worst_right_attempts: # move on topper side
            l = mid + 1
        else:
            h = mid -1
        count = min(count, temp)
    memo[key] = count
    return count

eggs = 2
floors = 100

attempts = Solve(eggs, floors, {})
print('# of attempts: ', attempts)