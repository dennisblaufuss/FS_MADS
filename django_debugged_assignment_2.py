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
        # Tail is used in a few functions for faster result
        self.tail = self.head = Node(data)
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

        # Version for classic linekd list (=without tail):
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

# time complexity SOPHIE

# Creating a LL


def createlist(n):  # nicht als funktion wenn wir das net brauchen
    LL = LinkedList(0)
    i = 1
    while i <= n:
        LL.add(i)
        i += 1
    # print(LL)
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
            input_df["List"][i].insert(1, 42)  # @Dennis:
            # can you refactor the code so we cann insert from position 0 onwards?
        time_span = perf_counter_ns() - time_start
        input_df["Time_Span"][i] = time_span/1000000000  # time in sec
        i += 1


insert_df(df, 500000)

# Line Plot

df_plot = pd.DataFrame(df)

# plot
# Dimension and Style of the Chart
plt.figure(figsize=(16, 5))
plt.style.use("ggplot")

plt.plot(df_plot["Count"], df_plot["Time_Span"],
         marker="o",
         color="red",
         label="Time Span")

# Labeling and aligning the axes to 0
plt.xlabel("Amount of elements inserted")
plt.xlim(xmin=0)
plt.ylabel("Time Span in Seconds")
plt.ylim(ymin=0, ymax=2)
plt.title("Calculate time complexity to insert elements into a linked list")
plt.show()


# Time Complexity PHILIPP


i = 10000  # <--- creation of the linked list
n = 20000  # <--- quantity to insert
l = 1000000  # <--- max linked list length
reps = 50  # <--- number of times the 'at' gets repeated to get an average time

data_count = []
data_time1 = []
data_time2 = []

while i <= l:
    new_lst = LinkedList()

    for j in (range(i)):
        new_lst.add(j)

    time_start1 = perf_counter_ns()
    for k in range(reps):
        new_lst.at(randrange(i))
    time_end1 = perf_counter_ns()
    time_span1 = time_end1 - time_start1
    time_in_sec_1 = (time_span1 / 1000000000) / reps
    print(
        f"To access a random element in a linked list of size {i} it takes on avg. {time_in_sec_1} Seconds")

    data_count.append(i)
    data_time1.append(time_in_sec_1)

    time_start2 = perf_counter_ns()
    for j in range(n):
        new_lst.insert(1, j)
        j += 1

    time_end2 = perf_counter_ns()
    time_span2 = time_end2 - time_start2
    time_in_sec_2 = time_span2 / 1000000000
    print(
        f"To insert {n} elements in a set of {i} elements it takes {time_in_sec_2} Seconds")

    data_time2.append(time_in_sec_2)

    i = 10*i

data = {"count": data_count,
        "time (access)": data_time1, "time (insert)": data_time2}

df = pd.DataFrame(data)

print(df)
