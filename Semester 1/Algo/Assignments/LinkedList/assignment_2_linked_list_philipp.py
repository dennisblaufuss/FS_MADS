from time import perf_counter_ns
from random import randrange
import matplotlib.pyplot as plt
import pandas as pd


class Node:
    def __init__(self, data=None):
        self.data = data  # Assign data
        self.next = None  # Initialize
        # the last element always has his next pointer set to None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, data=None):
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

    def insert(self, index, data):
        current_index = 0
        new_node = Node(data)
        current = self.head
        while current.next is not None:
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
        return self.size

# time complexity

i = 10
count = []
time = []
data = []
while i <= 100000:
    count.append(i)
    test = LinkedList()

    for j in (range(i)):
        test.add(j)

    time_start = perf_counter_ns()
    for k in range(100):
        test.at(randrange(i))

    time_end = perf_counter_ns()
    time_span = time_end - time_start
    time_in_sec_10000 = time_span / 1000000000
    time.append(time_in_sec_10000)
    data = {"Count": count, "Time_Span": time}
    # print(f"i: {i} takes {time_in_sec_10000} Seconds")
    i = 10*i

df = pd.DataFrame(data)

# plot
# Dimension and Style of the Chart
plt.figure(figsize=(16,5))
plt.style.use("ggplot")

plt.plot(df["Count"], df["Time_Span"],
        marker = "o",
        color = "red",
        label = "Time Span")

# Labeling and aligning the axes to 0
plt.xlabel("Amount of elements inserted")
plt.xlim(xmin=0)
plt.ylabel("Time Span in Seconds")
plt.ylim(ymin=0)
plt.title("Calculate time complexity to insert elements into a linked list")
plt.show()