from copy import copy
import sys
import string


class Queue:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def push(self, data):
        newItem = QueueItem(data)
        if (self.root == None):
            self.root = newItem
            return
        newItem.next = self.root
        self.root = newItem
        return newItem

    def pop(self):
        if (self.isEmpty()):
            return
        tempReturn = copy(self.root)
        temp = self.root
        self.root = temp.next
        temp = None
        tempReturn.makeUppercase()
        return tempReturn


class QueueItem:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data

    def makeUppercase(self):
        self.data = string.capwords(self.data)


queue = Queue()
for line in sys.stdin:
    line = line.rstrip()
    queue.push(line)
