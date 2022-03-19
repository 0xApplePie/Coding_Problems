# this works on normal currencies
# e.g.: [1,2,5,10,20,50,100,200,500,1000] 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        number_coins = 0
        rest = amount
        
        if rest == 0:
            return number_coins
        
        for coin in coins:
            number_coins += rest // coin
            rest = rest % coin
            print(coins, coin, number_coins, rest)
        if rest != 0:
            return -1
        
        return number_coins