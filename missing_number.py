class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums2 = [item for item in range(0,len(nums)+1)]
        return set(nums2).difference(set(nums)).pop()
        