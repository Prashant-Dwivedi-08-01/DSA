
#! Valid of String with only '(' and ')'

class Solution:
    def canBeValid(self, s: str) -> bool:
        # if number of characters are odd then can be valid, number of '(' == number of ')'
        if(len(s) & 1):
            return False
        
        # checking the balance of string from left to right. From left to right, the parenthesis 
        # string is said to be balanced if at any time/position we have no_of_( > no_of_).
        balance = 0
        for index, ch in enumerate(s):
            if ch == '(' or ch == '{': # if ch=')' and locked is 0, that means we can change that ')' to '('
                balance+=1
            else:
                balance-=1
        
            if balance < 0:
                return False
        
        #checking from right to left
        balance = 0
        n = len(s)-1
        while(n >= 0):
            if s[n] == ')' or s[n] == '}':
                balance += 1
            else:
                balance -= 1
        
            if balance  < 0:
                return False
            n-=1
                
        return True


sol = Solution()
s = '(()))'
print(sol.canBeValid(s))