class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode()
        p = self.head
        for i in range(1,capacity):
            node = ListNode()
            p.next,p = node,p.next

    def get(self, key: int) -> int:
        while not self.head:
            if not self.head.val.get(key):
                #最新访问的放到单链表最后
                value = self.head.val.get(key)

                return value
            else:
                head = head.next
        return -1



    def put(self, key: int, value: int) -> None:
        pass


if __name__ == "__main__":
    capacity = 10
    key, value = 1, "a"
    obj = LRUCache(capacity)
    param_1 = obj.get(key)
    obj.put(key, value)
