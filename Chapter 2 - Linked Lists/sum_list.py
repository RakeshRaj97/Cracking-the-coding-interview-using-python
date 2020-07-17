# method to sum given two single linked list where each node contains a single digit
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

    def reverse_recursive(self):
        prev = None
        cur_node = self.head
        while cur_node:
            nxt = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = nxt
        self.head = prev

    def length(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def sum(self, list):
        l1 = self.length()
        l2 = list.length()
        diff = abs(l1-l2)

        if l1 == l2:
            pass
        elif l1 < l2:
            for i in range(diff):
                l1.append(0)
        else:
            for i in range(diff):
                l2.append(0)

        p = self.head
        q = list.head
        carry = 0
        sum_list = LinkedList()

        while p or q:
            add = p.data + q.data + carry

            if add >= 10:
                carry = 1
                remainder = add % 10
                sum_list.append(remainder)
            else:
                carry = 0
                sum_list.append(add)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_list.print_list()


llist = LinkedList()
llist.append(5)
llist.append(6)
llist.append(3)

llist2 = LinkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)

llist.sum(llist2)
