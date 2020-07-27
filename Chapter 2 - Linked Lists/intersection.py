# method to determine if the two singly linked list intersect
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


    def intersection(list1, list2):

        shorter = list1 if list1.length() < list2.length() else list2
        longer = list1 if list1.length() > list2.length() else list2

        diff = longer.length() - shorter.length()

        shorter_node, longer_node = shorter.head, longer.head
        for i in range(diff):
            longer_node = longer_node.next

        while shorter_node is not longer_node:
            shorter_node = shorter_node.next
            longer_node = longer_node.next

        return shorter_node

list1 = LinkedList()
list1.append("A")
list1.append("B")
list1.append("C")
list1.append("D")
list1.append("E")
list1.append("F")
list1.append("G")

list2 = LinkedList()
list1.append("A")
list1.append("B")
list1.append("C")
list1.append("D")
list1.append("E")
list1.append("F")
list1.append("G")

list3 = LinkedList()
list3.append("A")
list3.append("B")
list3.append("C")
list3.append("E")

print(list1.intersection(list2))
