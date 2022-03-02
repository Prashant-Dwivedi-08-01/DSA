# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/
class Solution:
    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        return self.solve(digits, mapping, "", [])
    
    def solve(self, digits, mapping, present_ans, result):
        if len(digits) == 0:
            result.append(present_ans)
            return result
        for char in mapping[digits[0]]: # a for digit = 1
            new_present = present_ans + char
            result = self.solve(digits[1:], mapping, new_present, result)
        
        return result

obj = Solution()
ans = obj.letterCombinations("23")
print(ans)