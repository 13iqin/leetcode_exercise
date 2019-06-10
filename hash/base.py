"""
1.实现一个基于链表法解决散列冲突的散列表
2.实现一个LRU缓存淘汰算法:基于数组；基于列表；加上哈希表查找链表元素
"""


class LinkedNode:

    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache:

    # hash表里存的是前一个结点
    # 比如如果链表是1->2->3
    # 那么哈希表里hash[2]=1
    # @param capacity, an integer
    def __init__(self, capacity):
        self.hash = {}
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity

    # 在链表尾插入（链表尾的元素为最近使用的）
    def push_back(self, node):
        self.hash[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    # 在链表头删除
    def pop_front(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next
        self.hash[self.head.next.key] = self.head

    # change "prev->node->next...->tail"
    # to "prev->next->...->tail->node"
    def kick(self, prev):
        node = prev.next
        if node == self.tail:
            return
        prev.next = node.next
        if node.next is not None:
            self.hash[node.next.key] = prev
            node.next = None
        self.push_back(node)

    # @return an integer
    def get(self, key):
        if key not in self.hash:
            return -1
        self.kick(self.hash[key])
        # 因为hash[key]指向该结点的前一个结点，所以需要加上.next
        return self.hash[key].next.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # 若缓存中有这个数据了，则将它优先级提到最高（删除后加到链表尾）
        if key in self.hash:
            self.kick(self.hash[key])
            self.hash[key].next.value = value
        # 若缓存中没这个数据，加到链表尾
        else:
            self.push_back(LinkedNode(key, value))
            if len(self.hash) > self.capacity:
                self.pop_front()