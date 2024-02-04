class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        count = 0
        for i in range(len(word1)):
            ans= ans + word1[i]
            if i< len(word2):
                ans= ans + word2[i]
            count = i
        if count+1<len(word2):
            for j in range(count+1,len(word2)):
                ans= ans + word2[j]
        return ans


        