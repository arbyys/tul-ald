class Queue:
    def __init__(self):
        self.root = None

    def enqueue(self, data):
        if (self.root == None):
            self.root = QueueItem(data)
            return
        
        pass

    def dequeue(self):
        pass


class QueueItem:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
