class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        node = ListNode(0)
        self.head, self.tail = node, node
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail and self.tail.prev == self.head
        
    def append(self, value: int) -> None:
        node = ListNode(value)
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        node.next = self.tail

    def appendleft(self, value: int) -> None:
        node = ListNode(value)
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev= self.head

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        node = self.tail.prev
        self.tail.prev.prev.next = self.tail
        self.tail.prev = node.prev
        return node.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        node = self.head.next
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        return node.val        
