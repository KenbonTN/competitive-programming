class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = ''
        ans = []
        for i in digits:
            nums+=(str(i))
        newNum = int(nums) + 1

        for i in str(newNum):
            ans.append(int(i))

        return ans