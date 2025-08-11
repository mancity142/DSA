class Solution:
    def checkSolution(self,nums:set[int])->bool:
        hashset=set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
