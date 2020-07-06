# method to implement linked list using python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Prev_node not in list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


list = LinkedList()
list.append("B")
list.append("D")
list.append("E")
list.append("F")

list.prepend("A")

list.insert_after_node(list.head.next, "C")
list.print()