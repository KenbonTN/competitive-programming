class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_sum_map = defaultdict(int)
        ans = []
        min_sum = len(list1) + len(list2)
        for i in range(len(list1)):
            if list1[i] in list2:
                index_sum_map [list1[i]] = list2.index(list1[i]) + i
                min_sum = min(min_sum , list2.index(list1[i]) + i)

        print(index_sum_map)
        for i in index_sum_map:
            if index_sum_map[i] == min_sum:
                ans.append(i)
        return ans




        