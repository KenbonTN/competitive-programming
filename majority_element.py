from collections import Counter
import  math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_hash = Counter(nums)
        ans = []
        for i in count_hash:
            if count_hash[i] > math.floor((len(nums)/3)):
                ans.append(i)
        return ans

        