class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = list(range(1, n+1))
        start=0
        to_be_removed=0
        while(len(nums)>1):
            to_be_removed = (start + k-1)%len(nums)
            nums.pop(to_be_removed)
            start=to_be_removed
        return nums[0]