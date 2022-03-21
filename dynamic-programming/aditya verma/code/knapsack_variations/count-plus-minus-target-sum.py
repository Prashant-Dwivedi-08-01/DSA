#
#* Logic is simple. Exactly same as Mimum Difference Subset
#* Here, when we reach the last element we check if are forming the desired sum, then we say
#* that we can make this desired sum using some combination of +,- on given elements of array

def helper(array, n, desired_sum, current_sum):

    if(n<=0):
        if current_sum == desired_sum:
            return 1
        else:
            return 0

    return helper(array, n-1 , desired_sum, current_sum + array[n-1]) \
           + helper(array, n-1, desired_sum, current_sum - array[n-1])

array = [1,1,2,3]
n = len(array)
desired_sum = 1
current_sum = 0
print(helper(array,n,desired_sum, current_sum))