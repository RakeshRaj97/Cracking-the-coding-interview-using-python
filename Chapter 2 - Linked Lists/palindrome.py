# method to check if a linked list is a palindrome
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

    def check_palindrome(self):
        # Method 1
        # p = self.head
        # s = ''
        # while p:
        #     s += p.data
        #     p = p.next
        # return s == s[::-1]

        # Method 2
        p = self.head
        s = []
        while p:
            s += p.data
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True


list1 = LinkedList()
list1.append("R")
list1.append("A")
list1.append("C")
list1.append("E")
list1.append("C")
list1.append("A")
list1.append("R")

list2 = LinkedList()
list2.append("A")
list2.append("B")
list2.append("C")

print(list1.check_palindrome())
print(list2.check_palindrome())

