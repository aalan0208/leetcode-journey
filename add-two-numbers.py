# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Solution is to go through each linked list from the start, add them and return the linked list
"""
 
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        dummy_head = ListNode(0) # create a fake start node for the result list 
        current_value = dummy_head # current value is a pointer that will move along the result list as we build it, initally it points to the dummny node 
        carry = 0 # Store the carry from addition for example if we add 6+4 = 10, 1 will be the carry, initially there is no carry so the carry is 0
         
        while l1 or l2 or carry: # while there is a node in l1 or l2 or carry is not zero, even if both lists end, we still process the last carry 
            value1 = l1.val if l1 else 0 
            value2 = l2.val if l2 else 0
            
            """
            divmod(x,10)
            divmod(a,b) returns (a // b, a % b), i.e. quotient and remainder
            
            Ex: val1 +val2 + carry = 17
            carry becomes 1 (17 // 10 )
            sum becomes 7 (17 % 10)
            
            """
            carry, sum = divmod(value1 + value2 + carry,10) 
            current_value.next = ListNode(sum) # Create a new node holding the digit sum and link it to the current node's next
            current_value = current_value.next # move current value foward to this newly created node, so the next digit will be appended after it
            
            l1 = l1.next if l1 else None # if l1 still has a node, move to the next one, if its already None, keep it none
            l2 = l2.next if l2 else None # if l1 still has a node, move to the next one, if its already None, keep it none
            
        return dummy_head.next #dummy head was fake first node with value 0. The real result list starts from dummy_head.next
            