#method to delete a node in the middle of a single linked list
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
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def delete_middle(self):
        length = self.length()
        length = round(length/2)
        cur_node = self.head
        count = 1

        while cur_node:
            if count == length:
                cur_node = cur_node.next

            print(cur_node.data)
            cur_node = cur_node.next
            count += 1

list = LinkedList()
list.append("A")
list.append("B")
list.append("C")
list.append("D")
print(list.length())
list.delete_middle()