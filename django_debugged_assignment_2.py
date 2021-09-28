from time import perf_counter_ns
from random import randrange
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class Node: 
    def __init__(self, data=None):
        self.data = data  # Assign data
        self.next = None  # Initialize with next empty pointer

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, data=None):  # Data can be None type as well to create empty list
        self.tail = self.head = Node(data)  # Tail is used in a few functions for faster result
        self.size = 1

    def __str__(self):
        data = ""
        current_node = self.head
        while current_node is not None:
            data += str(current_node.data) + " -> "
            current_node = current_node.next
        return data[:-4]

    def add(self, data):
        self.tail.next = Node(data)
        self.tail = self.tail.next
        self.size += 1
        return

        # Version for classic linked list (=without tail):
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self.size += 1
        return

    def at(self, index):
        if index >= self.size:
            raise Exception(f'Index {index} out of bound')
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def insert(self, index, data):
        pointer = []
        current_index = 0
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            last = current
            current = current.next
            if current_index == index:
                pointer = last.next
                last.next = new_node
                new_node.next = pointer
                self.size += 1
                return
            current_index += 1

    def remove(self, index):
        if index >= self.size:
            raise Exception(f'Index {index} out of bound')
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        for i in range(index - 1):
            current = current.next
        if current.next is self.tail:
            self.tail = current
        current.next = current.next.next
        self.size -= 1
        return

    def __len__(self):
        return self.size

    def substring(self, start, end, step=None):
        if start > end:
            return "not possible"
        if step is None:
            step = 1
        end -= 1
        if end > self.size:
            end = self.size
        data = ""
        current_node = self.head
        if start > 0 and step > 0:
            i = 0
            while i < start:
                current_node = current_node.next
                i += 1
        if step > 0:
            while start < end:
                data += str(current_node.data) + " -> "
                current_node = current_node.next
                start += step
            return data[:-4]
        else:
            return "negative step is only possible in double linked list"

    def __getitem__(self, slicer):
        if isinstance(slicer, slice):
            return "no clue wie dat geht"
        else:
            return self.at(slicer)
