def grid_traveller_print_path(n, m, present_path):
    if n == 1 and m == 1:
        print(present_path)
        return
    
    if n != 1:
        grid_traveller_print_path(n-1, m, present_path + "D")
    if m != 1:
        grid_traveller_print_path(n, m-1, present_path + "R")

#! Different way of returning the array List. Here, we are not maintaing the result array
#! But we are making new array from the results of both/all the calls and returning it as a result
#! of present call to the previous call
def grid_traveller_return_path(n, m, present_path):
    if n == 1 and m == 1:
        new_path = []
        new_path.append(present_path)
        return new_path
    
    new_path = []
    if n != 1:
        new_path.extend(grid_traveller_return_path(n-1, m, present_path + "D"))
    if m != 1:
        new_path.extend(grid_traveller_return_path(n, m-1, present_path + "R"))
    return new_path


n = 3
m = 3
path = grid_traveller_return_path(n, m, "")
print(path)

