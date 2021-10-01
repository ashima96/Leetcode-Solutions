class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for st in stones:
            if st in jewels:
                count +=1
        return count
        

jewels = "aA"
stones = "aAAbbbb"
solution = Solution()
print(solution.numJewelsInStones(jewels, stones))