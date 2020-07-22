# method to partition a linkedlist around the value of x
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

    def partition(self, x):
        before = before_head = Node(0)
        after = after_head = Node(0)
        cur_node = self.head

        while cur_node:
            if cur_node.data < x:
                before.next = cur_node
                before = before.next
            else:
                after.next = cur_node
                after = after.next

            cur_node = cur_node.next

        after.next = None
        before.next = after_head.next

        llist = before_head.next
        while llist:
            print(llist.data)
            llist = llist.next


list = LinkedList()
list.append("2")
list.append("1")
list.append("3")
list.append("2")
list.append("5")
list.append("2")
list.append("1")

print(list.partition("3"))