class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first_word = ''.join(word1)
        second_word = ''.join(word2)
        if first_word == second_word:
            return True
        else:
            return False 

        