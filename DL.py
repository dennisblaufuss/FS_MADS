from time import perf_counter_ns
from random import randrange


class DoublyNode:  # Style guide: convention how to write code - Capitalize first letter
    # Class is the blueprint

    # Function to initialize the node for double linked list
    def __init__(self, data=None, prev=None, next=None):  # always store "self"
        self.data = data  # Assign data 
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class DoublyLinkedList: 

    # Function to initialize the Double Linked List
    # List objects
    def __init__(self, data=None):  # This will create the first element of the Double Linked list
        self.head = DoublyNode(data)
        self.tail = self.head
        self.size = 1

    def __str__(self):   
        data = ""
        current_node = self.head
        while current_node is not None:
            data += str(current_node.data) + " <-> "
            current_node = current_node.next
        return data

    def add(self, data):
        # adds new node to the tail
        to_add_node = DoublyNode(data, self.tail, None)
        self.tail.next = to_add_node
        self.tail = to_add_node
        self.size += 1

    def at(self, index): # This will call the at-func for the Double Linked list
        if self.size / 2 >= index:
            return self.at_from_head(index)
        return self.at_from_tail(index)
    
        
    def at_from_head(self, index): # This will count elements of the DL starting from the head of the list
        if index >= self.size:
            raise Exception(f'Index {index} out of bound')
        current = self.head
        for i in range(index):
            current = current.next
        return current
    
    def at_from_tail(self, index): # This will count elements of the DL starting from the tail of the list
        if index >= self.size:
            raise Exception(f'Index {index} out of bound')
        current = self.tail
        c1 =  self.tail
        for i in range(self.size - index - 1):
            current = current.prev
        return current

    def insert(self, index, data):
        # 3 cases:
        # insert node in the beginning if index == 0
        # insert node in the end of the list
        # insert node between elements of the list
        if index == 0:
            to_add_node = DoublyNode(data, None, self.head)
            self.head = to_add_node
        elif index >= self.size:
            to_add_node = DoublyNode(data, self.tail, None)
            self.tail = to_add_node
        else: 
            tmp_index_node = self.at(index)
            before_tmp_index_node = tmp_index_node.prev
            to_add_node = DoublyNode(data, before_tmp_index_node, tmp_index_node)
            tmp_index_node.prev = to_add_node
            before_tmp_index_node.next = to_add_node
        self.size += 1
        
        
    def remove(self, index):
        # 3 cases:
        # removing node from the beginning of the list if index == 0
        # removing node from the end of the list
        # removing node between elements of the list
        if index == 0 and self.size == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index >= self.size:
            self.tail = self.tail.prev
            self.tail.next = None
        else: 
            to_remove_node = self.at(index)
            before_to_remove_node = to_remove_node.prev
            after_to_remove_node = to_remove_node.next
            before_to_remove_node.next = after_to_remove_node
            after_to_remove_node.prev = before_to_remove_node
        self.size -= 1
        
    def __len__(self):
        return self.size  


# time complexity

i = 10
while i <= 10000000:
    test = DoublyLinkedList()

    for j in (range(i)):
        test.add(j)

    time_start = perf_counter_ns()
    for k in range(100):
        test.at(randrange(i))

    time_end = perf_counter_ns()
    time_span = time_end - time_start
    time_in_sec_10000 = time_span / 1000000000
    print(f"i: {i} takes {time_in_sec_10000} Seconds")

    i = 10*i