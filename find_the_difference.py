class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        elements_count = {}
        for i in range(len(s)):
            if s[i] not in elements_count:
                elements_count[s[i]]=1
            else: 
                elements_count[s[i]]+=1
        for i in t:
            if i not in elements_count:
                return i
            else:
                elements_count[i]-=1
        for i in elements_count.keys():
            if elements_count[i] != 0:
                return i