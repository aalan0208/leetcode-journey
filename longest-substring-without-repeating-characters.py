class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        characterSet = set() # This is an empty set, this will hold all unique characters currently inside the sliding window
        left_pointer = 0 # left pointer marks beginning of substring 
        result = 0 # the max length of the substring 
        
        for right_pointer in range(len(s)): # right pointer moves across the string 
            while s[right_pointer] in characterSet: # if the character is in the character set
                characterSet.remove(s[left_pointer]) # remove the left most character in the character set
                left_pointer += 1 #increment the left pointer
            characterSet.add(s[right_pointer]) # add character if not in character set 
            result = max(result, right_pointer - left_pointer + 1) # get the max value against the current result and the distance between the pointers and store in result
        return result # return the max value