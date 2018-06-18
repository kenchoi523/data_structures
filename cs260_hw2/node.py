class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        result = "[ " + str(self.value) + " ]"
        return result

    def getNext(self):
        return self.next

    def setNext(self, n):
        self.next = n

    def getValue(self):
        return self.value

    def setValue(self, v):
        self.value = v
