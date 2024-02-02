class Solution:
    def isPalindrome(self, x: int) -> bool:
        tempo = x
        if x < 0: 
            return False
        str_x = str(x)
        reverse = ''
        for i in range(-1,-len(str_x)-1,-1):
            reverse+=str_x[i]
        reverse = int(reverse)
        if x-reverse == 0:
            return True