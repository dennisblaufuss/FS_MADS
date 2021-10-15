from time import perf_counter_ns
from random import randrange
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Node:  # Style guide: convention how to write code - Capitalize first letter
    # Class is the blueprint

    # Function to initialize the node object
    def __init__(self, data=None):  # always store "self"
        self.data = data  # Assign data
        self.next = None  # Initialize
        # next as null
        # the last element always has his next pointer set to None

    def __str__(self):
        return str(self.data)


class LinkedList:  # Look up PEP 20 & PEP 8

    # Function to initialize the Linked
    # List object
    def __init__(self, data=None):  # This will create the first element of the list
        self.head = Node(data)
        self.tail = self.head
        self.size = 1

    def __str__(self):
        data = ""
        current_node = self.head
        while current_node is not None:
            data += str(current_node.data) + " -> "
            current_node = current_node.next
        return data

    def add(self, data):
        # New Element of Class Node with our data input
        self.tail.next = Node(data)
        self.tail = self.tail.next
        self.size += 1

    def at(self, index):
        if index >= self.size:
            raise Exception(f'Index {index} out of bound')
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def insert(self, index, data): #@Dennis
        #could you refactor the code so that we can insert element at pos. 0?
        #so far, we insert the elements at pos. 1, bc 0 throws an error
        # example_list.insert(1,42)
        current_index = 0
        new_node = Node(data)
        current = self.head
        while current.next is not None:  # Loop durch die Linked List
            if current_index == index - 1:
                temp = current.next
                current.next = new_node
                new_node.next = temp
                self.size += 1
                return
            current = current.next
            current_index += 1
        raise Exception(f'Index {index} out of bound')

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

        # falls wir den letzten knoten löschen wollen, müssen wir unser self.tail aktuell halten
        if current.next is self.tail:
            self.tail = current

        current.next = current.next.next
        self.size -= 1

    def __len__(self):
        return self.size  # better precompute than recompute ;)

# time complexity

# Creating a LL 

def createlist(n):
    LL = LinkedList(0)
    i = 1
    while i <= n:
        LL.add(i)
        i +=1
    #print(LL)
    return LL

# Creating a df for input (includes count of elements, LL, and space for TC)

LL_count = []
LL_list = []

i = 5e3
j = 0
n = 10

while j < n:
    count = i
    LL_count.append(count)
    LL_list.append(createlist(count))
    i *= 2
    j += 1

data = {"Count": LL_count, "List": LL_list,
        "Time_Span": list(range(0, n))}

df = pd.DataFrame(data, index=list(range(0, n)))

#df_simulated = df

def insert_df(input_df, e):
    i = 0
    n = len(input_df.index)
    while i < n:
        time_start = perf_counter_ns()
        for pos in range(e):
            input_df["List"][i].insert(1,42) #@Dennis:
            #can you refactor the code so we cann insert from position 0 onwards?
        time_span = perf_counter_ns() - time_start
        input_df["Time_Span"][i] = time_span/1000000000 #time in sec
        i += 1
        
insert_df(df, 500000)

# Line Plot

df_plot = pd.DataFrame(df)

# plot
# Dimension and Style of the Chart
plt.figure(figsize = (16,5))
plt.style.use("ggplot")

plt.plot(df_plot["Count"], df_plot["Time_Span"],
        marker = "o",
        color = "red",
        label = "Time Span")

# Labeling and aligning the axes to 0
plt.xlabel("Amount of elements inserted")
plt.xlim(xmin = 0)
plt.ylabel("Time Span in Seconds")
plt.ylim(ymin = 0, ymax = 2)
plt.title("Calculate time complexity to insert elements into a linked list")
plt.show()

