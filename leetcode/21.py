# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_list = []
        while l1 or l2:
            if l1 and l2 and l1.val < l2.val:
                new_list.append(l1.val)
                l1 = l1.next
            elif l1 and l2 and l1.val == l2.val:
                new_list = new_list + [l1.val, l2.val]
                l1 = l1.next
                l2 = l2.next
            elif l2:
                new_list.append(l2.val)
                l2 = l2.next
            elif l1:
                new_list.append(l1.val)
                l1 = l1.next
        l = None
        while len(new_list) > 0:
            l = ListNode(new_list.pop(), l)
        return l
                