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
        
    if(weight[no_of_items-1] <= capacity):
        if no_of_items-1 in memo.keys():
            return memo[no_of_items-1]

        include_present_item_value = value[no_of_items-1]

        memo[no_of_items-1] = max(
            include_present_item_value + knapsack(weight, value, no_of_items-1, capacity-weight[no_of_items-1], memo),
            knapsack(weight, value, no_of_items-1, capacity, memo)
        )

        return memo[no_of_items-1]
  
    elif weight[no_of_items-1] > capacity:
        memo[no_of_items-1] = knapsack(weight, value, no_of_items-1, capacity, memo)
        return memo[no_of_items-1]

no_of_items=30
weight = [1,3,2,4,5,2,9,7,8,4,1,2,5,9,6,3,5,8,9,10,50,60,3,9,8,2,1,2,6,9]
value =  [1,3,2,4,5,2,9,7,8,4,1,2,5,9,6,3,5,8,9,10,50,60,3,9,8,2,1,2,6,9]
capacity = 200

memo = {}
print(knapsack(weight, value, no_of_items, capacity, memo))