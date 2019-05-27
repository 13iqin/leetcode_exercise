# Definition for a Node.

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # 输入1->2->3->None
        # 则中间结果为1->1(copy)->2->2(copy)->3->3(copy)->None
        # 返回1(copy)->2(copy)->3(copy)->none

        save = head
        # 构造中间链表
        while (head != None):
            new = RandomListNode(head.label)
            new.next = head.next
            head.next = new
            head = new.next
        # 取得random指针
        head = save
        while (head != None):
            if (head.random != None):
                head.next.random = head.random.next
            else:
                head.next.random = None
            head = head.next.next
        head = save.next
        # 取得最终链表
        while (head != None):
            if (head.next == None):
                head.next = None
                break
            else:
                head.next = head.next.next
                head = head.next
        return save.next


node1 = RandomListNode(1)
# node2 = RandomListNode(2)
# node1.next = node2
s = Solution()
result = s.copyRandomList(node1)
while (result != None):
    print(result.label)
