
"""
LOGIC: Make a count array whose size is equal to maximum element + 1
This array stores the count of elements. Eg: count_arr[5] means count of 5 in 
input array.

Now loop over the count array and keep appending the index of count array in sorted array the 
number of times it is present.
Eg: input = [1,2,1]

count_arr = [0,2,1]

then sorted array has index 1 repeated 2 times then index 2 repeated 1 time and index 0 repeated 0 times
sorted_arr = [1, 1, 2]

*Tutorial
https://www.hackerearth.com/practice/algorithms/sorting/counting-sort/tutorial/

*TIME: O(N + K) k is the max element
"""
def count_sort(arr):
    # find max element O(n)
    mx = max(arr)

    # declare arr of size mx + 1
    count_arr = [0 for i in range(mx + 1)]

    # loop over arr and store the count of each ele
    for i in arr:
        count_arr[i] += 1
    
    # declare a sorted arr which will be the ans
    sorted_arr = []

    # loop over the count_arr and fill the sorted arr as per the logic
    for i in range(mx+1):
        temp = count_arr[i] # what is the count of element i

        # keep apending i for temp number of times viz. count of i in arr
        while temp > 0:
            sorted_arr.append(i)
            temp -= 1    

    return sorted_arr

if __name__ == "__main__":
    arr = [3,9,4,1,4,2,90]
    ans = count_sort(arr)
    print(ans)