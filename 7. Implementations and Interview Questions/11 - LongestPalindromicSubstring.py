class Solution:

    def longestPalindrome(self, s):
        result = ""        
        for i in range(len(s)):
            word1 = self.checkPalindrome(s, i, i)
            word2 = self.checkPalindrome(s, i, i+1)
            
            if len(word1) >= len(word2):
                longest = word1
            else:
                longest = word2
                
            if len(longest) >= len(result):
                result = longest
            else:
                result = result
            
        return result          
        
            
    def checkPalindrome(self, s, left, right):
        
        while left >= 0 and right < len(s) and s[left]==s[right]:
            left -= 1
            right += 1
        
        return s[left+1:right]