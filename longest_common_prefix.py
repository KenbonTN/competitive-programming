class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_string = sorted(strs, key= len)
        ans = ""

        # iterating over the first string in the sorted list
        for index, char in enumerate(sorted_string[0]):
            flag = True

            # iterate to find the common prefixes 
            for word in sorted_string[1:]:
                if word[index] != char:
                    flag=False
                    break
            if flag == True:
                ans += char
            else:
                break
        return ans
