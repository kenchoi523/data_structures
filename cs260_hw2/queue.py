from node import *


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        if self.empty():
            return "Queue Empty"
        else:
            current = self.first
            result = ""
            while current is not None:
                result = result + str(current)
                current = current.getNext()
            return result

    def front(self):
        return self.first.getValue()

    def empty(self):
        if self.first is None:
            return True
        else:
            return False

    def enqueue(self, x):
        new = Node(x)
        if self.first is None and self.last is None:
            self.first = new
            self.last = self.first
        else:
            self.last.setNext(new)
            self.last = new

    def dequeue(self):
        if self.first is None:
            return
        elif self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = self.first.getNext()
