import random as rd
from time import perf_counter_ns
import pandas as pd
import matplotlib.pyplot as plt


def merge(r_list, l_list):
    # help function for merge sort
    return_list = []
    i = 0
    j = 0
    while i < len(r_list) and j < len(l_list):
        if r_list[i] < l_list[j]:
            return_list.append(r_list[i])
            i += 1
        elif r_list[i] > l_list[j]:
            return_list.append(l_list[j])
            j += 1
        else:
            return "list cannot contain duplicates"
    return_list += r_list[i:]
    return_list += l_list[j:]
    return return_list


def merge_sort(input_list):
    # basic merge sort
    if len(input_list) < 2:
        return input_list
    mid = len(input_list)//2
    r_list = merge_sort(input_list[mid:])
    l_list = merge_sort(input_list[:mid])
    return merge(r_list, l_list)


class KeyValue:
    # help class for creating BST
    def __init__(self, key, value=int):
        self.key = key
        self.value = value

    def __str__(self):
        return self.key

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key


class Node:
    # class for creating Nodes & BST
    def __init__(self, key, value=int):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def get(self, key):
        # returns value attached to given key
        if self.key < key:
            if self.right is None:
                return "Can't find the key " + str(key)
            return self.right.get(key)
        elif self.key > key:
            if self.left is None:
                return "Can't find the key " + str(key)
            return self.left.get(key)
        return self.value

    def dumb_insert(self, key, value):
        # inserts without balancing (hence dumb)
        if self.key == key:
            self.value = value
            return
        else:
            if self.key < key:
                if self.right is None:
                    self.right = Node(key, value)
                else:
                    self.right.dumb_insert(key, value)
            if self.key > key:
                if self.left is None:
                    self.left = Node(key, value)
                else:
                    self.left.dumb_insert(key, value)

    def flatten(self):
        # flattens the BST to a linked list (self.left is allways none)
        if self is None or self.left is None and self.right is None:
            return
        if self.left is not None:
            self.left.flatten()
            temp_right = self.right
            self.right = self.left
            self.left = None
            temp = self.right
            while temp.right is not None:
                temp = temp.right
            temp.right = temp_right
        self.right.flatten()

    def decompose(self):
        # creates list containing all Nodes of the BST
        self.flatten()
        dec_l = []
        while self:
            dec_l.append(KeyValue(self.key, self.value))
            if self.right:
                self = self.right
            else:
                break
        return dec_l

    def insert(self, key, value):
        # inserts with rebalancing (firstly decomposing it)
        # the new BST has to be assigned (i found no other way of doing it)
        ins_l = self.decompose()
        ins_l.append(KeyValue(key, value))
        return create_binary_search_tree(ins_l)

    def display(self):
        # displaying the BST graphically
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        # help function for display
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def cbst_help(in_l):
    # help function BST: creating a balanced BST
    if len(in_l) == 0:
        return None
    mid = len(in_l)//2
    tree = Node(in_l[mid].key, in_l[mid].value)
    tree.left = cbst_help(in_l[:mid])
    tree.right = cbst_help(in_l[mid + 1:])
    return tree


def create_binary_search_tree(in_l):
    # sorting input list & returning balanced BST
    sorted_l = merge_sort(in_l)
    return cbst_help(sorted_l)


# SHOWCASE "INTELLIGENT" INSERTION
in_len = 30
in_l = []
i = 0
# i steps defined as 2 to better show the insertion (& rebalancing)
while i < in_len:
    temp_key = "Dennis" + "_" + str(i).zfill(2)
    temp_val = rd.randrange(18, 105)
    temp = KeyValue(temp_key, temp_val)
    in_l.append(temp)
    i += 2
rd.shuffle(in_l)

tree = create_binary_search_tree(in_l)
tree.display()

# balanced tree with new Node
tree2 = tree.insert("Dennis_15", 420)
tree2.display()

# TIME COMPLEXITY
# creating list of nodes
data_count = []
data_list = []
n = 10
i = 0
j = 1
while i < n:
    count = j * 20000
    data_count.append(count)
    ii = 0
    in_l = []
    while ii < count:
        ii_str = str(ii)
        temp_key = "Dennis" + "_" + ii_str.zfill(6)
        temp_val = rd.randrange(18, 105)
        temp = KeyValue(temp_key, temp_val)
        in_l.append(temp)
        ii += 1
    # no random shuffle here so that we don't have to merge sort
    data_list.append(in_l)
    j *= 2
    i += 1

# creating data frame
data = {"Count": data_count, "Datalist": data_list, "BST": list(range(0, n)), "Timespan": list(range(0, n))}
# list(range(0, n)) as placeholder -> ugly but works :D
df = pd.DataFrame(data, index=list(range(0, n)))

i = 0
while i < len(df.index):
    # creating BST out of prev created data lists
    df["BST"][i] = cbst_help(df["Datalist"][i])
    start_time = perf_counter_ns()
    j = 0
    while j < 20000:
        # getting the values of the last 20000 Nodes of each BST and timing it (commented out)
        # df["BST"][i].get(df["Datalist"][i][df["Count"][i] - (j + 1)].key)
        # getting the values of 20000 random but not unique Nodes of each BST and timing it
        df["BST"][i].get(df["Datalist"][i][rd.randint(0, df["Count"][i] - 1)].key)
        j += 1
    end_time = perf_counter_ns()
    time_span = end_time - start_time
    df["Timespan"][i] = format(time_span/1e9, '.5f')
    i += 1
print(df)

plt.figure(figsize=(16, 5))
plt.style.use("ggplot")

plt.plot(df["Count"]/1e6, df["Timespan"],
         marker="o",
         color="red",
         label="Time to access nodes")

# Labeling and aligning the axes to 0
plt.xlabel("Nodes per BST in millions")
plt.xlim(xmin=0)
plt.ylabel("Timespan in seconds")
plt.ylim(ymin=0)
plt.title("Time for retrieving " + str(j) + " arbitrary elements from BSTs with increasing sizes")
plt.show()
