class Heap:
    def __init__(self):
        self.heap = []
        self.last = 0

    def __str__(self):
        return str(self.heap)

    def makenull(self):
        self.heap = []
        self.last = 0

    def insert(self, x):
        self.heap.append(x)
        self.last += 1
        if self.last == 2:
            if self.heap[1] < self.heap[0]:
                self.swap(0, 1)
        elif self.last >= 3:
            self.upheap(self.last)

    def parent(self, i):
        return (i-1)//2

    def left(self, i):
        return (i+1)*2 - 1

    def right(self, i):
        return (i+1)*2

    def swap(self, a, b):
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp

    def upheap(self, i):
        while i // 2 > 0:
            if self.heap[i - 1] < self.heap[(i // 2) - 1]:
                self.swap(((i // 2) - 1), (i - 1))
            i = i // 2

    def downheap(self, i):
        while (i * 2) + 2 < self.last:
            if self.left(i) is not None or self.right(i) is not None:
                if self.heap[self.left(i)] < self.heap[self.right(i)]:
                    temp = self.left(i)
                else:
                    temp = self.right(i)
            if self.heap[i] > self.heap[temp]:
                self.swap(temp, i)
            i = temp

    def inorder(self, i):
        if i < self.last:
            if self.left(i) is not None:
                self.inorder(self.left(i))
            if self.heap[i] is not None:
                print(str(self.heap[i]), end=" ")
            if self.right(i) is not None:
                self.inorder(self.right(i))

    def preorder(self, i):
        if i < self.last:
            if self.heap[i] is not None:
                print(str(self.heap[i]), end=" ")
            if self.left(i) is not None:
                self.preorder(self.left(i))
            if self.right(i) is not None:
                self.preorder(self.right(i))

    def postorder(self, i):
        if i < self.last:
            if self.left(i) is not None:
                self.postorder(self.left(i))
            if self.right(i) is not None:
                self.postorder(self.right(i))
            if self.heap[i] is not None:
                print(str(self.heap[i]), end=" ")

    def min(self):
        return self.heap[0]

    def deletemin(self):
        self.swap(0, self.last-1)
        result = self.heap.pop(self.last-1)
        self.last -= 1
        self.downheap(0)
        return result
