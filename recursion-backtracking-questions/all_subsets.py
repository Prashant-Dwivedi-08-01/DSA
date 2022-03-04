#
#!------------- PRINT All subsets ------------------
def print_all_subsets(string, present_subset):
    if len(string) == 0:
        print(present_subset)
        return
        
    
    ch = string[0]
    
    # include
    print_all_subsets(string[1:],present_subset + ch)
    # dont include
    print_all_subsets(string[1:],present_subset)

#!----------- Return All Subsets as List Array --------------
 
#* METHOD 1 *:  Return new array

#* Look at the logic of retruning
#* Here, at the end of the call(Base Condition) we append the present_ans
#* and return the present result array.
#* This returned array is used to updated the array at the previous call (Root Node)
#* Now this updated array is sent to next pass ( Right of the Root Node)
#* Right call updates the current result array and returns it back to root.
#* Root then returns it to the presivious call.

#LOOK AT THE IMAGE IN IMAGES FOR RETURN LOGIC 
def return_all_subsets_m1(string, present_subset, result_arr):
    if len(string) == 0:
        result_arr.append(present_subset)
        return result_arr
        
    
    ch = string[0]
    
    # include
    return_all_subsets_m1(string[1:],present_subset + ch,result_arr)
    # dont include
    return_all_subsets_m1(string[1:],present_subset,result_arr) # IMP to note here, we are sending the updated result_arr from left to this right call and thus append in right is done in updated list from left

    return result_arr


#* METHOD 2:  This is exact same as last method but here we dont return value from funnction but a result array is 
#* maintained outside the fucntion
def return_all_subsets_m2(string, present_subset, result_arr):
    if len(string) == 0:
        result_arr.append(present_subset)
        return
        
    
    ch = string[0]
    
    # include
    return_all_subsets_m2(string[1:],present_subset + ch,result_arr)
    # dont include
    return_all_subsets_m2(string[1:],present_subset,result_arr)

#* METHOD 3:  Different way of returning the array List. Here, we are not maintaing the result array
#*         But we are making new array from the results of both/all the calls and returning it as a result
#*         of present call to the previous call
def return_all_subsets_m3(string, present_subset):
    if len(string) == 0:
        new_array = []
        new_array.append(present_subset)
        return new_array
        
    
    ch = string[0]
    new_array = []
    
    # include
    new_array.extend(return_all_subsets_m3(string[1:],present_subset + ch)) 
    # dont include
    new_array.extend(return_all_subsets_m3(string[1:],present_subset))      

    return new_array  

string = "abc"
result = []
super_set = return_all_subsets_m3(string, "")
print(super_set)