def dice_roll(present_ans, target_sum, result):
    if target_sum == 0:
        result.append(present_ans)
        return result
    
    for i in range(1,7):
        if i <= target_sum:
            result = dice_roll(present_ans + str(i), target_sum-i, result)
    return result
target_sum = 4
ans = dice_roll("",target_sum, [])

print(ans)