class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        x=0
        for i in zip(*strs):
            if list(i)!=sorted(i):
                x+=1   
        return x
       