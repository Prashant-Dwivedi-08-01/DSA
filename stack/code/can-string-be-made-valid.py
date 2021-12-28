
#todo: LEETCODE PROBLEM: https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/
#* Very Good Solution Approach: https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/discuss/1650613/Intuition-Explained-oror-Balanced-Parentheses-Greedy-Approach-oror-C%2B%2B-Clean-Code


#! BASIC APPROACH/LOGIC :->
#! We move from left to right and keep incrementing balance if '(' and then keep decrementing 
#! balance if ')'. Same logic of stack, where we were pushing value(inc here) and removing the value(dec here).
#! And at any point if our stack becomes empty we say NOT VALID, stack empty means our balanced will become negative now!


#! Using the same logic here, we say that if we encounter ")" in left to right, ideally we must decr the balance, but if
#! If we have that poistion unlocked then we can swap it with  "("  and make out stirng valid if at all it becomes invalid 
#! anytime in future. Means, this position has an option, and thus this position should not be counted as invalid as it can
#! improve it self if becomes invalid

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # if number of characters are odd then can be valid, number of '(' == number of ')'
        if(len(s) & 1):
            return False
        
        # checking the balance of string from left to right. From left to right, the parenthesis 
        # string is said to be balanced if at any time/position we have no_of_( > no_of_).
        balance = 0
        for index, ch in enumerate(s):
            if ch == '(' or locked[index] == '0': # if ch=')' and locked is 0, that means we can change that ')' to '('
                balance+=1
            else:
                balance-=1
        
            if balance < 0:
                return False
        
        #checking from right to left
        balance = 0
        n = len(s)-1
        while(n >= 0):
            if s[n] == ')' or locked[n] == '0':
                balance += 1
            else:
                balance -= 1
        
            if balance  < 0:
                return False
            n-=1
                
        return True