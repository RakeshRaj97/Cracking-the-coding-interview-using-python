#method to find kth to last element in a single linked list
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

    def length(self):
        count = 0
        cur_node = self.head
        if self.head is None:
            return
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def kth_to_last(self, n):
        lenght = self.length()
        cur_node = self.head

        while cur_node:
            if lenght == n:
                return cur_node.data

            lenght -= 1
            cur_node = cur_node.next

            if cur_node is None:
                return

list = LinkedList()
list.append("A")
list.append("B")
list.append("C")
list.append("D")

print(list.kth_to_last(2))