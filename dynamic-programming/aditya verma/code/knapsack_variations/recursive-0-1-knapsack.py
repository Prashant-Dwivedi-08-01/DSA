'''
--------------------------LOGIC--------------------------
1) Choice Diagram
            Item
             |
            / \
           /   \
    Wt<=Cap      Wt>Cap ==> Dont Include
       |
      / \
     /   \
Include   Dont Include


2) We need to write the recursive code
{
    BASE CONDITION

    CHOICE DIAGRAM
}

3) The base condition here is if we dont have any item or our bag is full. How we came up to this because in
recursive code we keep giving the smaller inputs, and one time we will finish with number of items or bag capacity

4) Find the maximum profit among the two choices
    a) We include the present item and then try with other items
    b) We dont include the present item and then try other items
'''


def knapsack(weight, value, no_of_items, capacity):
    if capacity == 0 or no_of_items == 0:
        return 0 # max profit in this case is 0 as we dont have any time to add to sack or we dont have any space left to add any item

    # weight of last item in list is smaller than the actual capacity of the bag
    if(weight[no_of_items-1] <= capacity):
        include_present_item = value[no_of_items-1]
        return max(
            include_present_item + knapsack(weight, value, no_of_items-1, capacity-weight[no_of_items-1]),
            knapsack(weight, value, no_of_items-1, capacity)
        )
    # weight of last item in list is greater than the actual capacity of the bag
    elif weight[no_of_items-1] > capacity:
        return knapsack(weight, value, no_of_items-1, capacity)

no_of_items=30
weight = [1,3,2,4,5,2,9,7,8,4,1,2,5,9,6,3,5,8,9,10,50,60,3,9,8,2,1,2,6,9]
value =  [1,3,2,4,5,2,9,7,8,4,1,2,5,9,6,3,5,8,9,10,50,60,3,9,8,2,1,2,6,9]
capacity = 200
print(knapsack(weight, value, no_of_items, capacity))