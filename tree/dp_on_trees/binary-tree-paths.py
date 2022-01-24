# https://leetcode.com/problems/path-sum-ii/submissions/

class Solution:
    def pathSum(self, root, targetSum: int):
        if not root:
            return []
        all_results = []
        current_list =[]
        self.solve(root, targetSum, all_results, current_list)
        return all_results
    
    def solve(self, root, targetSum, all_results, current_list):
        if root == None:
            return
        if root.left == None and root.right == None:
            targetSum -= root.val
            if targetSum == 0:
                current_list_copy = current_list.copy()
                current_list_copy.append(root.val)
                all_results.append(current_list_copy) 
        else:
	    # HERE TARGETSUM IS IMMUTABLE DATATYPE. THUS WHEN WE PASS IT AHEAD IN NEXT FUNCTION CALL AND THEN BACKTRACK 
	    # TO THIS FUNCTINO CALL, THEN THE VALUE OF TAREGTSUM IN THIS FUNCTION CALL IS NOT CHANGED ANS IT REAMINS THE SAME.
        #     targetSum -= root.val  
	    # 
	    # HOWEVER CURRENT_LIST IS LIST DATAYPE WHICH IS A MUTABLE DATATYPE AND THUS WHEN WE PASS THE CURRENT_LIST OF 
	    # PRESENT FUNCTION CALL TO THE NEXT FUNCTION CALL AND UPDATE IT THERE THEN IT UPDATES THE CURRENT_LIST VALUES 
	    # HERE ALSO. FOR EXAMPLE, IF I APPEND ANY DATA IN NEXT FUNCTION CALL AND THEN BACKTRACK TO PRESENT FUNCTION CALL 
	    # THEN THE CURRENT LIST HERE WILL ALSO HAVE THE VALUE WHICH WAS INSERTED IN THE FUNCTION CALL WHICH DID JUST NOW 
	    # AND BACKTRACKED HERE. THUS WE NEED TO MANUALLY REMOVE THE VALUES FROM THE LIST SO THAT WE KEEP OUR LIST CONTENT
	    # SAME FOR EACH FUNCTION CALL
            current_list.append(root.val)
            self.solve(root.left, targetSum, all_results, current_list)
            self.solve(root.right, targetSum, all_results, current_list)
	    
	    # WE ARE REMOVING THE ABOVE VALUE WHICH WE INSERTED BECAUSE NOW THIS FUNCTION CALL IS ENDING AND WE WILL BACKTRACK TO
	    #  PREVIOUS FUNCTION CALL. THUS WE WILL REVERT BACK TO LAST FUNCTION CALL'S STATE
            current_list.pop() 