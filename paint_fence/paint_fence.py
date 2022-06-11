class Solution:
    def numWays(self, n: int, k: int) -> int:
        memo = {}
        
        def calc(i):
            if i == 1:
                return k
            if i == 2 :
                return k**2              
            if i in memo:
                return memo[i]
        
            memo[i] = (k-1) * ( calc(i-1) + calc(i-2) ) 
            
            return memo[i]
            
        return calc(n)