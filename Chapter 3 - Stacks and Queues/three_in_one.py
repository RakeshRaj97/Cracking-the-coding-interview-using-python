# method to implement three stacks in a single array
stacks = [[] for _ in range(3)]

stacks[0].append('A')
stacks[1].append('a')
stacks[2].append('1')
stacks[0].append('B')
stacks[1].append('b')
stacks[2].append('2')
stacks[0].append('C')
stacks[1].append('c')
stacks[2].append('3')
print(stacks)
stacks[0].pop()
stacks[1].pop()
stacks[2].pop()
print(stacks)