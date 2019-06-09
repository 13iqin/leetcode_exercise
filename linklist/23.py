# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        all_node = []
        for x in lists:
            while x is not None:
                all_node.append(x)
                x = x.next
        all_node_sort = sorted(all_node, key=lambda node: node.val)
        pHead = ListNode(-1)
        p = pHead
        for node in all_node_sort:
            p.next = node
            p = node
        p.next=None
        return pHead.next
