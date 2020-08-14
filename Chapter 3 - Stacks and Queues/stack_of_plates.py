# method to implement stack of plates
class StackofPlates:
    def __init__(self, capacity):
        #set main stack
        self.stacks = []
        if capacity < 1:
            raise NameError("A stack is greater than one.")
        else:
            self.capacity = capacity

    def push(self, item):
        if self.stacks == []:
            self.stacks.append([item])
        else:
            if len(self.stacks[-1]) >= self.capacity:
                self.stacks.append([item])
            else:
                self.stacks[-1].append(item)

    def pop(self):
        if self.stacks == []:
            raise NameError("Can't pop an empty stack")
        else:
            popped_data = self.stacks[-1][-1]
            if len(self.stacks[-1]) == 1:
                del self.stacks[-1]
            else:
                del self.stacks[-1][-1]
            return popped_data

    def popAt(self, index):
        if self.stacks == []:
            raise NameError("can't pop an empty stack")
        elif index-1 > len(self.stacks):
            raise NameError("index out of range")
        else:
            popped_data = self.stacks[index-1][-1]
            if len(self.stacks[index-1]) == 1:
                del self.stacks[-1]
            elif len(self.stacks) == index:
                del self.stacks[-1][-1]
            else:
                self.stacks[index-1][-1] = self.stacks[index][0]

                for i in range(index, len(self.stacks)):
                    # move each element up
                    for j in range(0, len(self.stacks[i])-1):
                        self.stacks[i][j] = self.stacks[i][j+1]
                    if i < len(self.stacks) - 1:
                        self.stacks[i][-1] = self.stacks[i+1][0]
                    #del self.stacks[-1][-1]
                    # if stack is empty delete it
                    if (self.stacks[-1]) == 0:
                        del self.stacks[-1]
            return popped_data

if __name__ == "__main__":
    s = StackofPlates(4)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    s.push(8)
    s.push(9)
    s.push(10)
    a = s.pop()
    print(a)
    b = s.popAt(1)
    print(b)