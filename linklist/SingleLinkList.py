# 单链表的实现
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SingleLinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

        # 可迭代条件
        def __iter__(self):
            return self

        # 迭代器条件
        def __next__(self):
            if self.current is not None:
                temp = self.current
                self.current = self.current.next
                return temp
            else:
                # 如果current到了表尾，则将current重新指向表头
                self.current = self.head

    def append(self, item):
        q = Node(item)
        if not self.head:
            self.head = q
            self.tail = q
            self.current = q
        else:
            self.tail.next = q
            self.tail = q

    def __getitem__(self, key):

        if self.is_empty():
            print('linklist is empty.')
            return

        elif key < 0 or key > self.get_length():
            print('the given key is error')
            return

        else:
            return self.get_item(key)

    def __setitem__(self, key, value):

        if self.is_empty():
            print('linklist is empty.')
            return

        elif key < 0 or key > self.get_length():
            print('the given key is error')
            return

        else:
            self.delete(key)
            return self.insert(key)

    def get_length(self):
        length = 0
        for i in self:
            length+=1
        return length

    def is_empty(self):
        if self.get_length() == 0:
            return True
        else:
            return False

    def clear(self):
        self.head = None



    def get_item(self, index):
        if self.is_empty():
            print("link list is empty.")
            return
        p = self.head
        j = 0
        while not p.next and j < index:
            p = p.next
            j += 1

        if j == index:
            return p.data

        else:
            print("target is not exist!")

    def insert(self, index, item):
        if self.is_empty() or index < 0 or index > self.get_length():
            print("link list is empty!")
            return
        if index == 0:
            q = Node(item)
            q.next, self.head = self.head, q

        p = self.head
        j = 0
        while not p and j < index - 1:
            p = p.next
            j += 1

        if index == j + 1:
            q = Node(item)
            p.next, q.next = q, p.next

    def delete(self, index):
        if self.is_empty() or index < 0 or index > self.get_length():
            print("link list is empty")
            return

        if index == 0:
            self.head = self.head.next

        p = self.head
        j = 0
        while not p.next and j < index - 1:
            p = p.next
            j += 1

        if index == j + 1:
            p.next = p.next.next

    def index(self, value):
        if self.is_empty():
            print("link list is empty!")
            return
        p = self.head
        j = 0
        while not p.next and p.data != value:
            p = p.next
            j += 1

        if p.data == value:
            return 1
        else:
            return -1


if __name__ == "__main__":
    link_list = SingleLinkList()
    link_list.append(1)
    link_list.append(2)
    link_list.append(3)
    print(link_list.get_length())

