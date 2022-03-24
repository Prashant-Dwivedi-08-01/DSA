
# Refer this video for explanation: https://www.youtube.com/watch?v=5P84A0YCo_Y&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=10
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ans = self.solve(n,k)
        return ans
    def solve(self, n, k):
        if n == 1 and k == 1:
            return 0
        
        mid = 2**(n -1)// 2
        if k <= mid:
            return self.solve(n-1, k)
        else:
            return 1 if self.solve(n-1, k-mid) == 0 else 0

n = 2
k = 2
obj = Solution()
ans = obj.kthGrammar(n,k)
print(ans)
