class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        left_pointer = 0 
        right_pointer = len(s) - 1
        
        for i in range(len(s)):
            