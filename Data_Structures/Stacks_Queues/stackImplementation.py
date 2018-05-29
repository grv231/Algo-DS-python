class Stack(object):

    # Constructor function of stack
    def __init__(self):
        self.items = []

    # isEmpty method to check the emptyness of stack
    def isEmpty(self):
        return self.items == []

    # Push method for pushing items on the stack
    def push(self,item):
        self.items.append(item)

    # Pop method for removing the elements in LIFO fashion
    def pop(self):
        return self.items.pop()

    # Peek function to check the top of stack without removing it
    def peek(self):
        return self.items[len(self.items) - 1]

    # Size function to calculate the size of stack
    def size(self):
        return len(self.items)