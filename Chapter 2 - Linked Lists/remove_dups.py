#method to remove duplicates in an unsorted linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node =  Node(data)

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

    def remove_dups(self):
        cur_node = self.head
        prev_node = None
        dup_values = dict()

        while cur_node:
            if cur_node.data in dup_values:
                prev_node.next = cur_node.next
                cur_node = None
            else:
                dup_values[cur_node.data] = 1
                prev_node = cur_node
            cur_node = prev_node.next

list = LinkedList()
list.append("A")
list.append("A")
list.append("B")
list.append("C")
list.append("C")

list.remove_dups()
list.print()
