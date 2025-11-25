class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        new_list = sorted(nums1 + nums2)
        left_number = 0
        right_number = 0
       
        if len(new_list) % 2 == 0:
            left_number = new_list[len(new_list) // 2 - 1]
            right_number = new_list[len(new_list) //2]
            return (left_number + right_number) / 2.0

        else:
            return new_list[len(new_list) // 2] * 1.0
            