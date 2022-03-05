# For Question: https://leetcode.com/problems/trapping-rain-water/
# SOLUTION: Look at the image in images
"""
Here we follow the simple logic that, we should calculate the water
above each building and then simply add all the water.

To calculate the water above any building, we know that water must be
trapped by the buildings of greater height on the either side of the present
building.
Eg: Here minimum of left and right is taken and we simply substract it from
the present height to know the water above.
   __
  |  |........... __
  |  |           |  |
  |  |   __      |  |
  |  |  |  |     |  |
  |  |  |  |     |  |
  |  |  |  |     |  |
   7     2         5
Water above 2 is Min(7,5) - 2 ==> 5-2 = 3 units

"""
def max_to_left(arr):
    ans = []
    ans.append(arr[0])
    # LOGIC: Here we traverse array one by one and keep appending the max to left 
    #        of current in current position. Eg: arr => 5,4,3 then ans => [5] then
    #        for position 2 we select the max of 4 and 5 so position 2 has max value
    #        possible from it's present position to entire of left. So in next step
    #        at position 3 we know that at position 2 is the maximum possible value at left
    #        and we have to compare just the present and last
    for num in arr[1:]:
        ans.append(max(ans[len(ans)-1], num))
    return ans 
def max_to_right(arr):
    ans = []
    ans.append(arr[len(arr)-1])
    for i in range(len(arr)-2, -1, -1):
        ans.append(max(ans[len(ans)-1], arr[i]))
    ans.reverse()
    return ans
def rain_water_trap(building):
    max_to_left_array = max_to_left(building)
    max_to_right_array = max_to_right(building)
    
    # selecting the min of the two for each building
    min_building = list(map(lambda x,y: min(x,y), max_to_left_array, max_to_right_array))

    water = list(map(lambda x, y: x-y, min_building, building))
    print(water)
    return sum(water)
buildings = [4,2,0,3,2,5]
print(rain_water_trap(buildings))