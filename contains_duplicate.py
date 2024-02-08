class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_num = set(nums)
        if len(new_num) == len(nums):
            return False
        else:
            return True

        
        

        