class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return str(self.data)


class DoublyLinkedList:

    length = 0
    head = Node(None, None, None)
    tail = Node(None, None, None)

    def clear(self):
        temp = self.head
        while temp is not None:
            temp_next = temp.next
            temp.next, temp.prev, temp.data = None, None, None
            temp = temp_next
        self.head, self.tail, self.length = None, None, 0
    
    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0
    
    def add(self, item):
        self.add_last(item)
    
    def add_new(self, item):
        self.head = Node(item, None, None)
        self.tail = self.head

    def add_last(self, item):
        if self.is_empty():
            self.add_new(item)
        else:
            self.tail.next = Node(item, self.tail, None)
            self.tail = self.tail.next
        self.length += 1
    
    def add_first(self, item):
        if self.is_empty():
            self.add_new(item)
        else:
            self.head.prev = Node(item, None, self.head)
            self.head = self.head.prev
        self.length += 1
    
    def peek_first(self):
        if self.is_empty():
            raise RuntimeError("Array is empty")
        return self.head
    
    def peek_last(self):
        if self.is_empty():
            raise RuntimeError("Array is empty")
        return self.tail
    
    def remove_first(self):
        if self.is_empty():
            raise RuntimeError("Array is empty")
        data = self.head.data
        self.head = self.head.next
        self.length -= 1

        if self.is_empty():
            self.tail = None
        else:
            self.head.prev = None
        
        return data
    
    def remove_last(self):
        if self.is_empty():
            raise RuntimeError("Array is empty")
        data = self.tail.data
        self.tail = self.tail.prev
        self.length -= 1

        if self.is_empty():
            self.head = None
        else:
            self.tail.next = None
        
        return data
    
    def remove(self, node: Node):
        if node.prev is None:
            return self.remove_first()
        
        if node.next is None:
            return self.remove_last()
        
        node.next.prev = node.prev
        node.prev.next = node.next

        data = node.data

        node.data = None
        node, node.prev, node.next = None, None, None

        self.length -= 1

        return data
    
    def remove_at(self, index):
        if index < 0 or index > self.length:
            raise RuntimeError("Illegal deletion attempted. Index smaller than 0 or greater than list")

        if index < self.length // 2:
            i = 0
            temp = self.head
            while i != index:
                temp = temp.next
                i += 1
        else:
            i = self.length - 1
            temp = self.tail 
            while i != index:
                temp = temp.prev
                i -= 1
        
        return self.remove(temp)
    
    def remove_val(self, value):
        temp = self.head
        while temp is not None:
            if temp.data == value:
                self.remove(temp)
                return True
            temp = temp.next
        return False
    
    def index_of(self, value):
        i = 0
        temp = self.head

        while temp is not None:
            if temp.data == value:
                return i
            temp = temp.next
            i += 1
        
        return -1
    
    def contains(self, value):
        return self.index_of(value) != -1
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        ll_str = '['
        temp = self.head
        while temp.next is not None:
            ll_str += str(temp.data) + ", "
            temp = temp.next
        ll_str += str(temp.data) + "]"
        return ll_str