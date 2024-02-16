class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("QWERTYUIOPqwertyuiop")
        row2 = set("ASDFGHJKLasdfghjkl")
        row3 = set("ZXCVBNMzxcvbnm")
        result = []
        for word in words:
            if all(letter in row1 for letter in word) or all(letter in row2 for letter in word) or all(letter in row3 for letter in word):
                result.append(word)
        return result
                 