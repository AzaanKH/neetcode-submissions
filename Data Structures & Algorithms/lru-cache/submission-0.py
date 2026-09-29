class ListNode:
    def __init__(self, key: int, val: int, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    # map is key to ListNode    

    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.add(self.map[key])
            return self.map[key].val
        return -1
    
    def add(self, node: ListNode):
        prevNode = self.tail.prev
        prevNode.next = node
        node.next = self.tail
        node.prev = prevNode
        self.tail.prev = node

    
    def remove(self, node: ListNode):
        nextNode = node.next
        prevNode = node.prev
        prevNode.next = nextNode
        nextNode.prev = prevNode
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        
        self.map[key] = ListNode(key, value)
        self.add(self.map[key])
        

        if len(self.map) > self.cap:
            removeNode = self.head.next
            self.remove(removeNode)
            del self.map[removeNode.key]
        
