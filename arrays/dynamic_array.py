class DynamicArray:

    def __init__(self, capacity):
        self.len = 0
        self.capacity = capacity
        self.items = [None for i in range(self.capacity)]
    
    def size(self):
        return self.len
    
    def get(self, index):
        return self.items[index]
    
    def set(self, index, item):
        self.items[index] = item 

    def clear(self):
        self.items = [None for i in range(self.len)]
    
    def add(self, item):
        if self.len + 1 >= self.capacity:
            if self.capacity == 0:
                self.capacity = 1
            else:
                self.capacity *= 2

            new_arr = [None for i in range(self.capacity)]
            for i in range(self.len):
                new_arr[i] = self.items[i]
        
            self.items = new_arr
        
        self.items[self.len] = item
        self.len += 1

    def __repr__(self): 
        return '[' + self.__str__() + ']'

    def __str__(self):
        arr_str = ''
        for i in range(self.len - 1):
            arr_str += str(self.items[i]) + ','
        return arr_str + str(self.items[self.len - 1])