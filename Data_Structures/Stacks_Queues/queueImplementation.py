class Queue(object):

    # Constructor function of queue
    def __init__(self):
        self.items = []

    # isEmpty method to check the emptyness of queue
    def isEmpty(self):
        return self.items == []

    # Enqueue method for insert items in the queue
    def enqueue(self,item):
        self.items.insert(0, item)

    # Dequeue method for removing the elements from queue in FIFO fashion
    def dequeue(self):
        return self.items.pop()

    # Size function to calculate the size of queue
    def size(self):
        return len(self.items)