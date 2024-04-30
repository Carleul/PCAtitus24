class Solution(object):
    def findWordsContaining(self, words, x):
        result = []

        for palavra in words:
            for letra in palavra:
                if letra == x:
                    result.append(words.index(palavra))
                    break
        return result