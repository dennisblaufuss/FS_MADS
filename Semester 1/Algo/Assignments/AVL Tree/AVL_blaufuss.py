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
        self.balance_factor = None
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

    def semi_balancing_insert(self, key, value):
        # inserts with rebalancing (firstly decomposing it)
        # the new BST has to be assigned (i found no other way of doing it)
        ins_l = self.decompose()
        ins_l.append(KeyValue(key, value))
        return create_binary_search_tree(ins_l)

    def basic_insert(self, key, value):
        # inserts without balancing (hence basic)
        # computes/updates BFs
        if self.key == key:
            self.value = value
            return
        else:
            if self.key < key:
                if self.right is None:
                    self.right = Node(key, value)
                    self.balance_factor = self.get_balance_factor()[1]
                    self.right.balance_factor = 0
                    # you clould compute this using get_balance_factor function but will be always 0
                else:
                    self.right.basic_insert(key, value)
                    self.balance_factor = self.get_balance_factor()[1]
            if self.key > key:
                if self.left is None:
                    self.left = Node(key, value)
                    self.balance_factor = self.get_balance_factor()[1]
                    self.left.balance_factor = 0
                    # see above
                else:
                    self.left.basic_insert(key, value)
                    self.balance_factor = self.get_balance_factor()[1]

    def balanced_insert(self, key, value):
        self.basic_insert(key, value)
        return self.balance()

    def get_balance_factor(self):
        # computes BF for node
        if self.left is None and self.right is None:
            height = 1
            balance_factor = 0
            return height, balance_factor
        elif self.right is None:
            height = 1 + self.left.get_balance_factor()[0]
            balance_factor = 1 - height
            return height, balance_factor
        elif self.left is None:
            height = 1 + self.right.get_balance_factor()[0]
            balance_factor = self.right.get_balance_factor()[0]
            return height, balance_factor
        else:
            height = 1 + max(self.left.get_balance_factor()[0], self.right.get_balance_factor()[0])
            balance_factor = self.right.get_balance_factor()[0] - self.left.get_balance_factor()[0]
        return height, balance_factor

    def balance(self):
        if self.balance_factor == 0:
            return
        elif self.balance_factor == 2:
            x = y = self
            if x.right.balance_factor == 2:
                y = x.right
            while x.right.right.balance_factor == 2:
                x = x.right
                y = x.right
            z = y.right
            return self.l_rotate(x, y, z)
        elif self.balance_factor == 1:
            if self.right.balance_factor == 2:
                x = self
                # if more unbalanced inserts than 1 this might be used (not necesary though)
                while x.right.right.balance_factor == 2:
                    x = x.right
                y = x.right
                z = y.right
                return self.l_rotate(x, y, z)
            else:
                self.right.balance()

        elif self.balance_factor == -2:
            x = y = self
            if x.left.balance_factor == -2:
                y = x.left
            while x.left.left.balance_factor == -2:
                x = x.left
                y = x.left
            z = y.left
            return self.r_rotate(x, y, z)
        elif self.balance_factor == -1:
            if self.left.balance_factor == -2:
                x = self
                while x.left.left.balance_factor == -2:
                    x = x.left
                y = x.left
                z = y.left
                return self.r_rotate(x, y, z)
            else:
                self.left.balance()

    def r_rotate(self, x, y, z):
        if z is not None:
            temp = z.right
            z.right = y
            y.left = temp
        y.balance_factor = y.get_balance_factor()[1]
        z.balance_factor = z.get_balance_factor()[1]
        if y != x:
            x.left = z
            x.balance_factor = x.get_balance_factor()[1]
            # in this case you don't have to rebind the tree since the root doesn't change
            # still the old root is returned -> so you can rebind in any case
            return x
        # in this case you have to rebind the tree since the root changes
        return z

    def l_rotate(self, x, y, z):
        if z is not None:
            temp = z.left
            z.left = y
            y.right = temp
        z.balance_factor = z.get_balance_factor()[1]
        y.balance_factor = y.get_balance_factor()[1]
        if y != x:
            x.right = z
            x.balance_factor = x.get_balance_factor()[1]
            # in this case you don't have to rebind the tree since the root doesn't change
            # still the old root is returned -> so you can rebind in any case
            return x
        # in this case you have to rebind the tree since the root changes
        return z

    def display(self):
        # displaying the BST graphically
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = f"{self.key} (BF: {self.balance_factor})"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = f"{self.key} (BF: {self.balance_factor})"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = f"{self.key} (BF: {self.balance_factor})"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = f"{self.key} (BF: {self.balance_factor})"
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
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


# example left left without changing root
print("example left left without changing root")
tree = Node("Deniz", 22)
tree.basic_insert("Bogdan", 27)
tree.basic_insert("Aylin", 24)
tree.basic_insert("Arben", 25)
tree.basic_insert("Bashkim", 22)
tree.basic_insert("Eren", 22)
tree.basic_insert("Zephir", 24)
tree.basic_insert("Yurin", 21)
tree.basic_insert("Zeynip", 23)
tree.basic_insert("Duran", 22)
tree.basic_insert("Can", 26)
tree.display()
# as mentioned you don't have to rebind since the root doesn't change
# you could though
tree.balanced_insert("Abdul", 29)
tree.display()

# example right right with changing root
print("example right right with changing root")
tree2 = Node("Deniz", 22)
tree2.basic_insert("Bogdan", 27)
tree2.basic_insert("Eren", 22)
tree2.basic_insert("Yurin", 21)
tree2.basic_insert("Duran", 22)
tree2.display()
# here you have to rebind as the root changes
tree3 = tree2.balanced_insert("Zeynip", 23)
tree3.display()
