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

def knapsack(weight, value, no_of_items, capacity, memo):
    
    if capacity == 0 or no_of_items == 0:
        return 0 
    
    key = (no_of_items-1, capacity)
    if key in memo.keys():
        return memo[key]

    if(weight[no_of_items-1] <= capacity):
        include_present_item_value = value[no_of_items-1]
        memo[key] = max(
            include_present_item_value + knapsack(weight, value, no_of_items-1, capacity-weight[no_of_items-1], memo),
            knapsack(weight, value, no_of_items-1, capacity, memo)
        )

        return memo[key]
  
    elif weight[no_of_items-1] > capacity:
        memo[key] = knapsack(weight, value, no_of_items-1, capacity, memo)
        return memo[key]

weight = [2,4,6,7,8] 
value =  [10,23,43,56,34]
capacity = 15
no_of_items=  len(weight)

memo = {}
print(knapsack(weight, value, no_of_items, capacity, memo))