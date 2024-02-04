class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1

        for i in dic:
            j = dic[i]
            cnt += j*(j-1)//2

        return cnt 

         
        