class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zeroes_index = []
        consecutive_ones_count = []
        if 1 not in nums:
            return 0
        if 0 not in nums:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes_index.append(i)
        for j in range(len(zeroes_index)-1):
            consecutive_ones_count.append(zeroes_index[j+1]-(zeroes_index[j]+1))
        consecutive_ones_count.append(len(nums)-(zeroes_index[-1]+1))
        if zeroes_index[0] != 0:
            consecutive_ones_count.append(zeroes_index[0])
        return max(consecutive_ones_count)

        # x = 0
        # if len(nums) == 1 and nums[0] == 1:
        #     return 1
        # elif 1 not in nums:
        #     return 0
        # for i in range(x,len(nums)-1):
        #     count = 1
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j] and nums[i] == 1:
        #             count+=1
        #         else:
        #             x = j
        #             break

        #     consecutive_count_list.append(count)
        # return max(consecutive_count_list)


        
        