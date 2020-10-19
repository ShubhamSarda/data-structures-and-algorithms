class Solution:
    def detectCapitalUse(self, word):
        count = 0
        length = len(word)

        for i in range(length):
            if word[i] >= chr(65) and word[i] < chr(91):
                count += 1

        if count == length:
            return True
        elif count == 0:
            return True
        elif count == 1 and word[0] >= chr(65) and word[0] < chr(91):
            return True
        else:
            return False