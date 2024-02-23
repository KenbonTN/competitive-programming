class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # element_hash = {}
        # for i, j in enumerate(nums):
        #     element_hash[i] = j
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] ==nums[j] and i*j % k == 0:
                    count = count + 1

        return count